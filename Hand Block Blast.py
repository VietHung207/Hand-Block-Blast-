import pygame
import os
from game_backend import GameLogic, HandTracker, WIDTH, HEIGHT, COLORS, GRID_SIZE, CELL_SIZE, GRID_OFFSET_X, GRID_OFFSET_Y, UI_START_X

DARK_BG = (18, 20, 32)
FRAME_BLUE = (35, 45, 70)
HIGHLIGHT_GLOW = (0, 220, 255)
SHADOW_COLOR = (0, 50, 100)
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Block Blast")
clock = pygame.time.Clock()

try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    boom_path = os.path.join(base_path, "boom.wav")
    click_path = os.path.join(base_path, "click.wav")
    
    sound_boom = pygame.mixer.Sound(boom_path)
    sound_click = pygame.mixer.Sound(click_path)
    
    sound_boom.set_volume(0.8)
    sound_click.set_volume(1.0)
    has_sound = True
    print(f"Đã tải nhạc từ: {base_path}")
except Exception as e:
    print("CẢNH BÁO LỖI NHẠC:", e)
    print("Hãy chắc chắn file boom.wav và click.wav nằm cùng thư mục với main.py")
    has_sound = False

try:
    ui_font = pygame.font.SysFont("Verdana", 28, bold=True)
    score_font = pygame.font.SysFont("Arial Black", 40, bold=True)
    title_font = pygame.font.SysFont("Arial Black", 60, bold=True) 
except:
    ui_font = pygame.font.SysFont("Arial", 28, bold=True)
    score_font = pygame.font.SysFont("Arial", 40, bold=True)
    title_font = pygame.font.SysFont("Arial", 60, bold=True)

logic = GameLogic()
tracker = HandTracker()

def draw_block(surf, x, y, color_idx, size=CELL_SIZE):
    rect = (x, y, size, size)
    pygame.draw.rect(surf, COLORS[color_idx], rect)
    pygame.draw.rect(surf, BLACK, rect, 2)

def draw_text_shadow(surf, text, font, col, col_shadow, x, y, align="center"):
    s_surf = font.render(text, True, col_shadow)
    f_surf = font.render(text, True, col)
    rect = f_surf.get_rect(center=(x, y)) if align == "center" else f_surf.get_rect(topleft=(x, y))
    surf.blit(s_surf, (rect.x+3, rect.y+3))
    surf.blit(f_surf, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: logic.state = "MENU"

    hand_data = tracker.get_hand_pos()
    px, py = hand_data["px"], hand_data["py"] 
    tx, ty = hand_data["tx"], hand_data["ty"] 
    pinching = hand_data["pinching"]

    screen.fill(DARK_BG)
    draw_text_shadow(screen, "HAND BLOCK BLAST", title_font, HIGHLIGHT_GLOW, SHADOW_COLOR, WIDTH//2, 50)

    if logic.state == "MENU":
        btns = [("NEW GAME", 300), ("RESUME", 400), ("QUIT", 500)]
        for text, y in btns:
            rect = pygame.Rect(WIDTH//2 - 120, y, 240, 70)
            col, txt_col, border = FRAME_BLUE, WHITE, HIGHLIGHT_GLOW
            
            if text == "RESUME" and not logic.game_started:
                col, txt_col, border = (30,30,40), (100,100,100), (50,50,60)
            
            elif rect.collidepoint(px, py):
                col = (70, 80, 120)
                if pinching:
                    if text == "NEW GAME": logic.reset_game()
                    if text == "RESUME" and logic.game_started: logic.state = "PLAYING"
                    if text == "QUIT": running = False
            
            pygame.draw.rect(screen, col, rect, border_radius=15)
            pygame.draw.rect(screen, border, rect, 3, border_radius=15)
            lbl = ui_font.render(text, True, txt_col)
            screen.blit(lbl, (rect.centerx - lbl.get_width()//2, rect.centery - lbl.get_height()//2))

    elif logic.state == "PLAYING" or logic.state == "GAMEOVER":
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x, y = GRID_OFFSET_X + c*CELL_SIZE, GRID_OFFSET_Y + r*CELL_SIZE
                pygame.draw.rect(screen, (100, 100, 100), (x, y, CELL_SIZE, CELL_SIZE), 1)
                if logic.grid[r][c]: draw_block(screen, x, y, logic.grid[r][c])

        draw_text_shadow(screen, f"SCORE: {logic.score}", score_font, WHITE, (50,50,50), UI_START_X, 150, "left")
        screen.blit(ui_font.render(f"BEST: {logic.high_score}", True, (255, 100, 100)), (UI_START_X, 210))

        if logic.state == "PLAYING":
            if pinching and not logic.holding:
                for i, blk in enumerate(logic.tray):
                    if blk and UI_START_X < px < WIDTH and 300 + i*140 < py < 430 + i*140:
                        logic.holding, logic.held_idx = True, i
            
            elif not pinching and logic.holding:
                gx, gy = (tx - GRID_OFFSET_X) // CELL_SIZE, (ty - GRID_OFFSET_Y) // CELL_SIZE
                blk = logic.tray[logic.held_idx]
                
                if logic.can_place(blk, gx, gy):
                    cleared = logic.place_block(blk, gx, gy)
                    
                    if has_sound:
                        if cleared > 0: sound_boom.play()
                        else: sound_click.play()

                    logic.tray[logic.held_idx] = None
                    if all(b is None for b in logic.tray): logic.tray = logic.new_tray()
                
                logic.holding, logic.held_idx = False, -1
            
            logic.check_game_over()

        for i, blk in enumerate(logic.tray):
            if blk and not (logic.holding and logic.held_idx == i):
                cx, cy = UI_START_X + 100, 300 + i*140
                for dx, dy in blk["shape"]: draw_block(screen, cx + dx*30, cy + dy*30, blk["color"], 30)

        if logic.holding:
            blk = logic.tray[logic.held_idx]
            gx, gy = (tx - GRID_OFFSET_X) // CELL_SIZE, (ty - GRID_OFFSET_Y) // CELL_SIZE
            valid = logic.can_place(blk, gx, gy)
            for dx, dy in blk["shape"]:
                col = (0, 255, 0) if valid else (255, 0, 0)
                pygame.draw.rect(screen, col, (GRID_OFFSET_X + (gx+dx)*CELL_SIZE, GRID_OFFSET_Y + (gy+dy)*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
                draw_block(screen, tx + dx*CELL_SIZE, ty + dy*CELL_SIZE, blk["color"])

    if logic.state == "GAMEOVER":
        ovl = pygame.Surface((WIDTH, HEIGHT)); ovl.set_alpha(200); ovl.fill(BLACK); screen.blit(ovl, (0,0))
        draw_text_shadow(screen, "GAME OVER", title_font, (255, 50, 50), (100, 0, 0), WIDTH//2, HEIGHT//2 - 50)
        hint = ui_font.render("Press ESC for Menu", True, WHITE)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2 + 30))

    if hand_data["detected"]:
        color = (255, 50, 50) if logic.holding else HIGHLIGHT_GLOW
        pygame.draw.line(screen, (80, 80, 120), (tx, ty), (px, py), 2)
        
        thumb_col = (0, 255, 0) if logic.holding else FRAME_BLUE
        pygame.draw.circle(screen, thumb_col, (tx, ty), 8)
        
        pygame.draw.circle(screen, DARK_BG, (px, py), 12)
        pygame.draw.circle(screen, color, (px, py), 10)
        pygame.draw.circle(screen, WHITE, (px, py), 12, 1)

    pygame.display.flip()
    clock.tick(240)

tracker.release()
pygame.quit()