import pygame

pygame.init() #초기화 (시작전 항상)

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PangPang Game") #게임 이름

# FPS
clock = pygame.time.Clock()
# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/Py files/PangPang/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/Py files/PangPang/character.png")
character_size = character.get_rect().size # 이미지 크기 설정
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 설정 - 캐릭터 절반에 위치 설정
character_y_pos = screen_height - character_height  #화면 세로 크기 가장 아래에 캐릭터 설정

#이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 2

# 적(스프라이트) enemy 캐릭터
enemy = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/Py files/PangPang/enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기 설정
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2 - (enemy_width / 2) # 화면 가로의 절반 크기에 설정 - 캐릭터 절반에 위치 설정
enemy_y_pos = screen_height / 2 - enemy_height / 2  #화면 세로 크기 가장 아래에 캐릭터 설정

# 폰트 설정
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트 스타일, 크기)

# 총 시간 설정
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현제 시작 tick을 받아오기

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 설정
    print("fps: " + str(clock.get_fps())) # 시각적 fps 확인

# 캐릭터가 100 만큼 이동을 해야하는데 [프레임에 따라 속도가 달라짐]
#10fps : 1초 동안에 10번 동작
#10fps : 2초 동안에 20번 동작 -> 1번에 4만큼 이동! 5 * 20 = 100 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # panal have a X button.  창이 닫히는 이벤트가 발생하였는게
            running = False # 거짓인 경우 진행중이 아님을 확인

        if event.type == pygame.KEYDOWN: # 키를 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed   
            if event.key == pygame.K_RIGHT:
                to_x += character_speed 
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
         character_y_pos = screen_height - character_height

    #충돌 처리를 위한 rect info update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크 처리
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    # screen.fill((0,0,255)) # I can use this fill to change  screen color
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    

    #타이머 설정
    #경과 시간 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과 시간을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) # 실제 화면에 시간 타이머 그리기
    #출력할 글자 설정, True, 글자 색상
    screen.blit(timer,(10,10))

    pygame.display.update() # 게임화면 다시 그리기! 이벤트 루트

# pygmae quit
# 팡게임 나가기
pygame.quit()