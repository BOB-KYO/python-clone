import pygame

pygame.init() #초기화 (시작전 항상)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PangPang Game") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/Py files/PangPang/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/loved/OneDrive/개인/Notebook_backup/Python Project/Py files/PangPang/character.png")
character_size = character.get_rect().size # 이미지 크기 설정
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 설정 - 캐릭터 절반에 위치 설정
character_y_pos = screen_height - character_height  #화면 세로 크기 가장 아래에 캐릭터 설정

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # panal have a X button.  창이 닫히는 이벤트가 발생하였는게
            running = False # 거짓인 경우 진행중이 아님을 확인
    # screen.fill((0,0,255))
    
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    pygame.display.update() # 게임화면 다시 그리기! 이벤트 루트

# pygmae quit
pygame.quit()