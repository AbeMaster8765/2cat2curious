def on_a_pressed():
    if hops_and_paws.vy == 0:
        hops_and_paws.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    game.set_game_over_effect(False, effects.melt)
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        deathbox
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.set_game_over_effect(True, effects.confetti)
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest
        """),
    on_overlap_tile2)

hops_and_paws: Sprite = None
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