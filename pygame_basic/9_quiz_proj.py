import random
import pygame
#Quiz) 하늘에서 떨어지는 똥 피하기 프래임을 만드시오

# #[게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS 는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (가로,세로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

#1. 팔레트(화면)초기화 만들기


pygame.init()

    #화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
    # ()는 튜퓰 값 고정

    #화면 타이틀 설정
pygame.display.set_caption("DDong Game") #창 이름표기

    #FPS
fps_clock = pygame.time.Clock()

#2. 사용자 게임 초기화

#배경
background = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/python-clone/PangPang/background.png")

#캐릭터
character = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/python-clone/PangPang/hero.png")
character_size = character.get_rect().size # 이미지 크기 설정
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 설정 - 캐릭터 절반에 위치 설정
character_y_pos = screen_height - character_height  #화면 세로 크기 가장 아래에 캐릭터 설정

#이동 좌표
move_x = 0
move_y = 0
#캐릭터 이동 속도
character_speed = 1

#적
enemy = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/python-clone/PangPang/ddong.png")

enemy_size = enemy.get_rect().size # 이미지 크기 설정
enemy_width = enemy_size[0] / 2 # 캐릭터의 가로 크기
enemy_height = enemy_size[1] / 2 # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0,screen_width - enemy_width) # 화면 가로의 절반 크기에 설정 - 캐릭터 절반에 위치 설정
enemy_y_pos = 0  #화면 세로 크기 가장 아래에 캐릭터 설정
enemy_speed = 8



running = True # 게임이 진행중인지 확인
while running:
    dt = fps_clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # panal have a X button.  창이 닫히는 이벤트가 발생하였는게
            running = False # 거깃인 경우 진행중이 아님을 확인

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                move_x += character_speed
        
        if event.type == pygame.KEYUP: # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                move_x = 0
               
    character_x_pos += move_x * dt 
    character_y_pos += move_y * dt


    #캐릭터 위치 정의
    

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    character_x_pos += move_x

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
         character_y_pos = screen_height - character_height

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)
    
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
    
    screen.fill((255,255,255)) # I can use this fill to change  screen color
    # screen.blit(background,(0,0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update()

pygame.quit()