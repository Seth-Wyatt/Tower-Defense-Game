from import_list import *

### Read the code carefully and you may find a hidden gem ;)

## Important variables ##

done = False
dead = False
start = False

money_required = 0
money = 0

enemy_1 = None
enemy_2 = None
enemy_3 = None
enemy_4 = None

enemy_count = 0
wave = 0
delay_counter = 0

bullets = []
bullet_list_pos = 0
bullet_delay = 0

# Sound
volume = 0.5
music_index = 0

pygame.init()

# Game Speed
speed_list = []
speed_list.extend([1.5, 2, 3, 0.5, 1])

speed = 1
speed_index = 0
game_run_speed = 60 * speed

# Setting up the sounds

background_music_list = []
background_music_list.extend(['Background_music_2.OGG', 'Background_music_1.OGG'])

home_screen_music_list = []
home_screen_music_list.extend(['Home_screen_music_1.OGG'])

pygame.mixer.music.load('Home_screen_music_1.OGG')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)

# Set screen parameters
screen_width = 700
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])

# Creates lists for the different block types

player_list = pygame.sprite.Group()

enemy_list_1 = pygame.sprite.Group()
enemy_list_2 = pygame.sprite.Group()
enemy_list_3 = pygame.sprite.Group()
enemy_list_4 = pygame.sprite.Group()
all_enemies_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

# Creates the "player"
player = Player(330, 230, 40, 40, BLUE, 1)

player_list.add(player)
all_sprites_list.add(player)

# Creates home screen and buttons

home_screen = HomeScreen(0, 0, screen_width, screen_height, BLACK, BROWN, 10, 'home_screen', "Tower Defense Game", 40)
start_button = Start(screen_width/2 - 150, 350, 300, 100, GREEN, BROWN, 10, 'start_button', "Start", 40)
start_settings = Settings(screen_width/2 - 150, 500, 300, 100, GREEN, BROWN, 10, 'start_settings', "Settings", 40)
easter_egg = EasterEgg(450, 20, 100, 10, BLACK, BLACK, 0, 'easter_egg', 'Find Me ;)', 25)
settings_screen = SettingsScreen(0, 0, screen_width, screen_height, BLACK, BROWN, 10, 'settings_screen', "", 40)
settings_box =Settings(0, 0, screen_width, 100, BROWN, BROWN, 10, 'start_settings', "WORK IN PROGRESS", 40)
start_volume_up = VolumeUp(15, 105, screen_width/2 - 20, 90, RED, WHITE, 5, 'start_volume_up', "Volume Up", 30, 0.5)
start_volume_down = VolumeDown(15, 210, screen_width/2 - 20, 90, RED, WHITE, 5, 'start_volume_down', "Volume Down", 30, 0.5)
start_back_button = BackButton(600, 450, 100, 50, GREEN, BLACK, 5, 'start_back_button', "Back", 30)

# Creates upgrades bar and buttons

upgrades_bar = UpgradesBar(0, 500, screen_width, 220, BLACK, BROWN, 5, 'upgrades_bar', "Upgrades_Bar", 14)
back_button = BackButton(600, 450, 100, 50, GREEN, BLACK, 5, 'back_button', "Back", 30)

health_upgrades = HealthUpgrades(10, 510, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'health_upgrades', "Health Upgrades", 40)
health_up = HealthUp(10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'health_up', "Health", 40)
recovery_up = RecoveryUp(screen_width/2 + 10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'recovery_up', "Recovery", 40)
damage_resist = DamageResist(10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'damage_resist',  "Damage Resist", 40)
block_chance = BlockChance(screen_width/2 + 10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'block_chance', "Block Chance", 40)

attack_upgrades = AttackUpgrades(screen_width/2 + 10, 510, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'attack_upgrades', "Attack Upgrades", 40)
dmg_up = DmgUp(10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'dmg_up', "Damage", 40)
attack_speed_up = AttackSpeedUp(screen_width/2 + 10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'attack_speed_up', "Attack Speed", 40)
crit_dmg = CritDmg(10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'crit_dmg',  "Crit Damage", 40)
crit_chance = CritChance(screen_width/2 + 10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'crit_chance', "Crit Chance", 40)

cash_upgrades = CashUpgrades(10, 620, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'cash_upgrades',  "Cash Upgrades", 40)
enemy_cash_up = EnemyCashUp(10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'enemy_cash_up', "Enemy Cash", 40)
boss_cash_up = BossCashUp(screen_width/2 + 10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'boss_cash_up', "Boss Cash", 40)
wave_cash_up = WaveCashUp(10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'wave_cash_up',  "Wave Cash", 40)
cash_multi = CashMulti(screen_width/2 + 10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'cash_multi', "Cash Multiplier", 40)

settings = Settings(screen_width/2 + 10, 620, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'settings', "Settings", 40)
game_speed = GameSpeed(10, 510, screen_width/4 - 20, 45, RED, WHITE, 5, 'game_speed', "Game Speed", 30)
volume_up = VolumeUp(10, 561, screen_width/4 - 20, 45, RED, WHITE, 5, 'volume_up', "Volume Up", 30, 1)
volume_down = VolumeDown(10, 613, screen_width/4 - 20, 45, RED, WHITE, 5, 'volume_down', "Volume Down", 30, 1)
background_music = BackgroundMusic(10, 665, screen_width/4 - 20, 45, RED, WHITE, 5, 'background_music', "Music", 30)


# Creates Health Bar
health_bar = HealthBar(screen_width/2 - ((screen_width-200)/2), 20, screen_width - 200, 30, GREY, player.max_health)
current_health_bar = HealthBar(screen_width/2 - ((screen_width-200)/2), 20, screen_width - 200, 30, RED, player.max_health)

dead_screen = DeadScreen(0, 0, screen_width, screen_height, BLACK, BROWN, 10, 'dead_screen', "Game Over", 40)
restart_button = Start(screen_width/2 - 150, 350, 300, 100, GREEN, BROWN, 10, 'restart_button', "Restart", 40)

clock = pygame.time.Clock()
# Main loop
current_menu = 'home_screen'
clicked_update_start_button = None
clicked_update_start_settings = None
clicked_update_start_back_button = None
clicked_update_easter_egg = None
clicked_update_start_volume_up = None
clicked_update_start_volume_down = None

clicked_update_restart_button = None

clicked_update_back_button = None

clicked_update_health = None

clicked_update_attack = None

clicked_update_cash = None

clicked_update_settings = None
clicked_update_volume_up = None
clicked_update_volume_down = None
clicked_update_background_music = None
clicked_update_game_speed = None

while not done:
    if dead:
        game_over_sound = pygame.mixer.Sound("Game_over_sound.ogg")
        game_over_sound.play()

    while dead:
        current_menu = 'dead_screen'
        dead_screen.draw(screen)
        restart_button.draw(screen)
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                dead = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=event.pos)

                clicked_update_restart_button = restart_button.click(mouse_event)
                if clicked_update_restart_button is not None and clicked_update_restart_button.id == 'restart_button' and current_menu == 'dead_screen':
                    done = False
                    dead = False
                    start = True

                    money = 0
                    money_required = 0

                    enemy_1 = None
                    enemy_2 = None
                    enemy_3 = None
                    enemy_4 = None

                    enemy_count = 0
                    wave = 0
                    delay_counter = 0

                    bullets = []

                    # Sound
                    volume = 0.5
                    music_index = 0

                    pygame.init()

                    # Game Speed
                    speed_list = []
                    speed_list.extend([1.5, 2, 3, 0.5, 1])

                    speed = 1
                    speed_index = 0
                    game_run_speed = 60 * speed

                    # Setting up the sounds

                    background_music_list = []
                    background_music_list.extend(['Background_music_2.OGG', 'Background_music_1.OGG'])

                    pygame.mixer.music.load('Background_music_1.OGG')
                    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
                    pygame.mixer.music.set_volume(volume)
                    pygame.mixer.music.play(-1)


                    # Set screen parameters
                    screen_width = 700
                    screen_height = 720
                    screen = pygame.display.set_mode([screen_width, screen_height])

                    # Creates lists for the different block types

                    player_list = pygame.sprite.Group()

                    enemy_list_1 = pygame.sprite.Group()
                    enemy_list_2 = pygame.sprite.Group()
                    enemy_list_3 = pygame.sprite.Group()
                    enemy_list_4 = pygame.sprite.Group()
                    all_enemies_list = pygame.sprite.Group()

                    all_sprites_list = pygame.sprite.Group()

                    # Creates the "player"
                    player = Player(330, 230, 40, 40, BLUE, 1)

                    player_list.add(player)
                    all_sprites_list.add(player)

                    # Creates home screen and buttons

                    home_screen = HomeScreen(0, 0, screen_width, screen_height, BLACK, BROWN, 10, 'home_screen', "Tower Defense Game", 40)
                    start_button = Start(screen_width/2 - 150, 350, 300, 100, GREEN, BROWN, 10, 'start_button', "Start", 40)
                    start_settings = Settings(screen_width/2 - 150, 500, 300, 100, GREEN, BROWN, 10, 'start_settings', "Settings", 40)
                    easter_egg = EasterEgg(450, 20, 100, 10, BLACK, BLACK, 0, 'easter_egg', 'Find Me ;)', 25)
                    settings_screen = SettingsScreen(0, 0, screen_width, screen_height, BLACK, BROWN, 10, 'settings_screen', "", 40)
                    settings_box =Settings(0, 0, screen_width, 100, BROWN, BROWN, 10, 'start_settings', "WORK IN PROGRESS", 40)
                    start_volume_up = VolumeUp(15, 105, screen_width/2 - 20, 90, RED, WHITE, 5, 'start_volume_up', "Volume Up", 30, 0.5)
                    start_volume_down = VolumeDown(15, 210, screen_width/2 - 20, 90, RED, WHITE, 5, 'start_volume_down', "Volume Down", 30, 0.5)
                    start_back_button = BackButton(600, 450, 100, 50, GREEN, BLACK, 5, 'start_back_button', "Back", 30)

                    # Creates upgrades bar and buttons

                    upgrades_bar = UpgradesBar(0, 500, screen_width, 220, BLACK, BROWN, 5, 'upgrades_bar', "Upgrades_Bar", 14)
                    back_button = BackButton(600, 450, 100, 50, GREEN, BLACK, 5, 'back_button', "Back", 30)

                    health_upgrades = HealthUpgrades(10, 510, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'health_upgrades', "Health Upgrades", 40)
                    health_up = HealthUp(10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'health_up', "Health", 40)
                    recovery_up = RecoveryUp(screen_width/2 + 10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'recovery_up', "Recovery", 40)
                    damage_resist = DamageResist(10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'damage_resist',  "Damage Resist", 40)
                    block_chance = BlockChance(screen_width/2 + 10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'block_chance', "Block Chance", 40)

                    attack_upgrades = AttackUpgrades(screen_width/2 + 10, 510, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'attack_upgrades', "Attack Upgrades", 40)
                    dmg_up = DmgUp(10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'dmg_up', "Damage", 40)
                    attack_speed_up = AttackSpeedUp(screen_width/2 + 10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'attack_speed_up', "Attack Speed", 40)
                    crit_dmg = CritDmg(10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'crit_dmg',  "Crit Damage", 40)
                    crit_chance = CritChance(screen_width/2 + 10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'crit_chance', "Crit Chance", 40)

                    cash_upgrades = CashUpgrades(10, 620, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'cash_upgrades',  "Cash Upgrades", 40)
                    enemy_cash_up = EnemyCashUp(10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'enemy_cash_up', "Enemy Cash", 40)
                    boss_cash_up = BossCashUp(screen_width/2 + 10, 510, screen_width/2 - 20, 90, RED, WHITE, 5, 'boss_cash_up', "Boss Cash", 40)
                    wave_cash_up = WaveCashUp(10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'wave_cash_up',  "Wave Cash", 40)
                    cash_multi = CashMulti(screen_width/2 + 10, 620, screen_width/2 - 20, 90, RED, WHITE, 5, 'cash_multi', "Cash Multiplier", 40)

                    settings = Settings(screen_width/2 + 10, 620, screen_width/2 - 20, 90, GREEN, WHITE, 5, 'settings', "Settings", 40)
                    game_speed = GameSpeed(10, 510, screen_width/4 - 20, 45, RED, WHITE, 5, 'game_speed', "Game Speed", 30)
                    volume_up = VolumeUp(10, 561, screen_width/4 - 20, 45, RED, WHITE, 5, 'volume_up', "Volume Up", 30, 1)
                    volume_down = VolumeDown(10, 613, screen_width/4 - 20, 45, RED, WHITE, 5, 'volume_down', "Volume Down", 30, 1)
                    background_music = BackgroundMusic(10, 665, screen_width/4 - 20, 45, RED, WHITE, 5, 'background_music', "Music", 30)


                    # Creates Health Bar
                    health_bar = HealthBar(screen_width/2 - ((screen_width-200)/2), 20, screen_width - 200, 30, GREY, player.max_health)
                    current_health_bar = HealthBar(screen_width/2 - ((screen_width-200)/2), 20, screen_width - 200, 30, RED, player.max_health)

                    dead_screen = DeadScreen(0, 0, screen_width, screen_height, BLACK, BROWN, 10, 'dead_screen', "Game Over", 40)
                    restart_button = Start(screen_width/2 - 150, 350, 300, 100, GREEN, BROWN, 10, 'restart_button', "Restart", 40)

                    clock = pygame.time.Clock()
                    # Main loop
                    current_menu = 'upgrades_bar'
                    clicked_update_start_button = None
                    clicked_update_start_settings = None
                    clicked_update_start_back_button = None
                    clicked_update_easter_egg = None
                    clicked_update_start_volume_up = None
                    clicked_update_start_volume_down = None

                    clicked_update_restart_button = None

                    clicked_update_back_button = None

                    clicked_update_health = None

                    clicked_update_attack = None

                    clicked_update_cash = None

                    clicked_update_settings = None
                    clicked_update_volume_up = None
                    clicked_update_volume_down = None
                    clicked_update_background_music = None
                    clicked_update_game_speed = None

        pygame.display.flip()
        clock.tick(game_run_speed)

    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                dead = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=event.pos)

                # In Game Attack Upgrades
                clicked_update_attack = attack_upgrades.click(mouse_event)
                if clicked_update_attack is not None and clicked_update_attack.id == 'attack_upgrades' and current_menu == 'upgrades_bar':
                    current_menu = 'attack_upgrades'

                # In Game Back Button
                clicked_update_back_button = back_button.click(mouse_event)
                if (clicked_update_back_button is not None and clicked_update_back_button.id == 'back_button' and current_menu in ['health_upgrades', 'attack_upgrades', 'cash_upgrades', 'settings']):
                    current_menu = 'upgrades_bar'

                # In Game Cash Upgrades
                clicked_update_cash = cash_upgrades.click(mouse_event)
                if clicked_update_cash is not None and clicked_update_cash.id == 'cash_upgrades' and current_menu == 'upgrades_bar':
                    current_menu = 'cash_upgrades'

                ## Easter Egg ##
                clicked_update_easter_egg = easter_egg.click(mouse_event)
                if clicked_update_easter_egg is not None and clicked_update_easter_egg.id == 'easter_egg' and current_menu == 'home_screen':
                    clicked_update_easter_egg.compliment()
                    clicked_update_easter_egg.colour = WHITE

                # Game Speed
                clicked_update_game_speed = game_speed.click(mouse_event)
                if clicked_update_game_speed is not None and clicked_update_game_speed.id == 'game_speed' and current_menu == 'settings':
                    speed = speed_list[speed_index]
                    game_run_speed = speed*60
                    speed_index += 1
                    if speed_index == len(speed_list):
                        speed_index = 0

                # In Game Health Upgrades
                clicked_update_health = health_upgrades.click(mouse_event)
                if clicked_update_health is not None and clicked_update_health.id == 'health_upgrades' and current_menu == 'upgrades_bar':
                    current_menu = 'health_upgrades'

                # In Game Settings
                clicked_update_settings = settings.click(mouse_event)
                if clicked_update_settings is not None and clicked_update_settings.id == 'settings' and current_menu == 'upgrades_bar':
                    current_menu = 'settings'

                # Start Button
                clicked_update_start_button = start_button.click(mouse_event)
                if clicked_update_start_button is not None and clicked_update_start_button.id == 'start_button' and current_menu == 'home_screen':
                    start = True
                    pygame.mixer.music.load('Background_music_1.OGG')
                    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
                    pygame.mixer.music.set_volume(volume)
                    pygame.mixer.music.play()
                    current_menu = 'upgrades_bar'

                # Start Settings
                clicked_update_start_settings = start_settings.click(mouse_event)
                if clicked_update_start_settings is not None and clicked_update_start_settings.id == 'start_settings' and current_menu == 'home_screen':
                    current_menu = 'start_settings'

                # Start Settings Back Button
                clicked_update_start_back_button = start_back_button.click(mouse_event)
                if clicked_update_start_back_button is not None and clicked_update_start_back_button.id == 'start_back_button' and current_menu == 'start_settings':
                    current_menu = 'home_screen'

                # Start Settings Volume Up
                clicked_update_start_volume_up = start_volume_up.click(mouse_event)
                if clicked_update_start_volume_up is not None and clicked_update_start_volume_up.id == 'start_volume_up' and current_menu == 'start_settings':
                    volume += 0.1
                    pygame.mixer.music.set_volume(volume)

                # Start Settings Volume Down
                clicked_update_start_volume_down = start_volume_down.click(mouse_event)
                if clicked_update_start_volume_down is not None and clicked_update_start_volume_down.id == 'start_volume_down' and current_menu == 'start_settings':
                    volume -= 0.1
                    pygame.mixer.music.set_volume(volume)

                # In Game Background Music
                clicked_update_background_music = background_music.click(mouse_event)
                if clicked_update_background_music is not None and clicked_update_background_music.id == 'background_music' and current_menu == 'settings':
                    song = background_music_list[music_index]
                    music_index += 1
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    if music_index == len(background_music_list):
                        music_index = 0

                # In Game Volume Up
                clicked_update_volume_up = volume_up.click(mouse_event)
                if clicked_update_volume_up is not None and clicked_update_volume_up.id == 'volume_up' and current_menu == 'settings':
                    volume += 0.1
                    pygame.mixer.music.set_volume(volume)

                # In Game Volume Down
                clicked_update_volume_down = volume_down.click(mouse_event)
                if clicked_update_volume_down is not None and clicked_update_volume_down.id == 'volume_down' and current_menu == 'settings':
                    volume -= 0.1
                    pygame.mixer.music.set_volume(volume)

        bullet_delay -= 1
        if bullet_delay <= 0:
            for i in range(1):
                if len(all_enemies_list) > 0:
                    # Create bullet targeting first enemy in list
                    e_target = all_enemies_list.sprites()[0]
                    bullet = Bullet(player.rect.centerx, player.rect.centery, 10, [e_target], bullets)

                    bullets.append(bullet)
                    bullet_delay = 60/player.fire_rate

        if delay_counter <= 6000 and start == True and dead != True:
            for x in range(2):
                if delay_counter == 0 + (wave*120):
                    p_target = player_list.sprites()[0]

                    enemy_1 = Enemy(0, 0, 21, 21, GREEN, 1, 2, 1, [p_target])
                    all_enemies_list.add(enemy_1)
                    enemy_list_1.add(enemy_1)
                    all_sprites_list.add(enemy_1)

                    enemy_2 = Enemy(0, 479, 21, 21, GREEN, 1, 2, 1, [p_target])
                    all_enemies_list.add(enemy_2)
                    enemy_list_2.add(enemy_2)
                    all_sprites_list.add(enemy_2)

                    enemy_3 = Enemy(679, 0, 21, 21, GREEN, 1, 2, 1, [p_target])
                    all_enemies_list.add(enemy_3)
                    enemy_list_3.add(enemy_3)
                    all_sprites_list.add(enemy_3)


                    enemy_4 = Enemy(679, 479, 21, 21, GREEN, 1, 2, 1, [p_target])

                    all_enemies_list.add(enemy_4)
                    enemy_list_4.add(enemy_4)
                    all_sprites_list.add(enemy_4)

                    wave += 1
                else:
                    delay_counter += 1

        if player.health <= 0:
            dead = True
            start = False

        screen.fill(WHITE)

        # Determines when blocks have collided
        enemy_hit_list = pygame.sprite.spritecollide(player, all_enemies_list, True)

        # Increases and decreases "health" when blocks are hit
        for enemy in enemy_hit_list:
            player.health -= enemy.damage

        # Prints "score" on screen
        font = pygame.font.SysFont('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*', 30, True, False)
        text = font.render(str(money), True, BLACK)

        # Where "score" text prints
        screen.blit(text, [630, 10])

        # Updates where sprites are and draws them
        all_sprites_list.update()
        all_sprites_list.draw(screen)

        ## DRAWS MENUS ##

        if current_menu == 'home_screen':
            home_screen.draw(screen)
            start_button.draw(screen)
            start_settings.draw(screen)
            easter_egg.draw(screen)
        elif current_menu == 'start_settings':
            settings_screen.draw(screen)
            start_volume_up.draw(screen)
            start_volume_down.draw(screen)
            settings_box.draw(screen)
            start_back_button.draw(screen)
        elif current_menu == 'upgrades_bar':
            upgrades_bar.draw(screen)
            health_upgrades.draw(screen)
            health_bar.draw(screen)
            current_health_bar.draw(screen)
            current_health_bar.update(player.health)
            attack_upgrades.draw(screen)
            cash_upgrades.draw(screen)
            settings.draw(screen)
        elif current_menu == 'health_upgrades':
            upgrades_bar.draw(screen)
            back_button.draw(screen)
            health_bar.draw(screen)
            current_health_bar.draw(screen)
            current_health_bar.update(player.health)
            health_up.draw(screen)
            recovery_up.draw(screen)
            damage_resist.draw(screen)
            block_chance.draw(screen)
        elif current_menu == 'attack_upgrades':
            upgrades_bar.draw(screen)
            back_button.draw(screen)
            health_bar.draw(screen)
            current_health_bar.draw(screen)
            current_health_bar.update(player.health)
            dmg_up.draw(screen)
            attack_speed_up.draw(screen)
            crit_dmg.draw(screen)
            crit_chance.draw(screen)
        elif current_menu == 'cash_upgrades':
            upgrades_bar.draw(screen)
            back_button.draw(screen)
            health_bar.draw(screen)
            current_health_bar.draw(screen)
            current_health_bar.update(player.health)
            cash_multi.draw(screen)
            wave_cash_up.draw(screen)
            boss_cash_up.draw(screen)
            enemy_cash_up.draw(screen)
        elif current_menu == 'settings':
            upgrades_bar.draw(screen)
            back_button.draw(screen)
            health_bar.draw(screen)
            current_health_bar.draw(screen)
            current_health_bar.update(player.health)
            game_speed.draw(screen)
            volume_up.draw(screen)
            volume_down.draw(screen)
            background_music.draw(screen)



        for bullet in bullets:
            bullet.draw(screen)
            bullet.update()

        pygame.display.flip()

        clock.tick(game_run_speed)

pygame.quit()