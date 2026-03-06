@namespace
class SpriteKind:
    Coin = SpriteKind.create()
    Flower = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap)

def on_a_pressed():
    if hops_and_paws.vy == 0:
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                400,
                600,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        hops_and_paws.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite2, location):
    game.set_game_over_effect(False, effects.melt)
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        deathbox
        """),
    on_overlap_tile)

def on_on_overlap2(sprite3, otherSprite2):
    global Bee
    sprites.destroy(otherSprite2)
    music.play(music.melody_playable(music.knock),
        music.PlaybackMode.IN_BACKGROUND)
    Bee = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    animation.run_image_animation(Bee, assets.animation("""
        Bee
        """), 100, True)
    Bee.set_position(hops_and_paws.x + 80, hops_and_paws.y - 80)
    Bee.follow(hops_and_paws, 50)
sprites.on_overlap(SpriteKind.player, SpriteKind.Flower, on_on_overlap2)

def on_overlap_tile2(sprite4, location2):
    game.set_game_over_effect(True, effects.confetti)
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest
        """),
    on_overlap_tile2)

def on_on_overlap3(sprite5, otherSprite3):
    sprites.destroy(otherSprite3)
    if hops_and_paws.y < Bee.y:
        info.change_score_by(3)
        music.play(music.melody_playable(music.small_crash),
            music.PlaybackMode.UNTIL_DONE)
    else:
        info.change_life_by(-1)
        music.play(music.melody_playable(music.buzzer),
            music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

Bee: Sprite = None
Flower2: Sprite = None
Coin2: Sprite = None
hops_and_paws: Sprite = None
info.set_life(4)
scene.set_background_color(9)
hops_and_paws = sprites.create(assets.image("""
    cat
    """), SpriteKind.player)
controller.move_sprite(hops_and_paws, 100, 0)
tiles.set_current_tilemap(tilemap("""
    Level
    """))
hops_and_paws.ay = 350
scene.camera_follow_sprite(hops_and_paws)
for value in tiles.get_tiles_by_type(assets.tile("""
    Coin
    """)):
    Coin2 = sprites.create(assets.image("""
        Coin
        """), SpriteKind.Coin)
    animation.run_image_animation(Coin2, assets.animation("""
        CoinSpin
        """), 100, True)
    tiles.place_on_tile(Coin2, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
        """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    FlowerPLACEHOLDER
    """)):
    Flower2 = sprites.create(assets.image("""
        Flower
        """), SpriteKind.Flower)
    tiles.place_on_tile(Flower2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
        """))

def on_on_update():
    hops_and_paws.set_image(assets.image("""
        cat
        """))
    if hops_and_paws.vy < 0:
        hops_and_paws.set_image(assets.image("""
            Cat Jumping
            """))
    elif hops_and_paws.vy > 0:
        hops_and_paws.set_image(assets.image("""
            Cat Falling
            """))
    if hops_and_paws.vx < 0:
        hops_and_paws.image.flip_x()
game.on_update(on_on_update)
