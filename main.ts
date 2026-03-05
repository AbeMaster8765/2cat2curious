controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (hops_and_paws.vy == 0) {
        music.play(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        hops_and_paws.vy = -150
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`deathbox`, function (sprite, location) {
    game.setGameOverEffect(false, effects.melt)
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`chest`, function (sprite, location) {
    game.setGameOverEffect(true, effects.confetti)
    game.gameOver(true)
})
let hops_and_paws: Sprite = null
game.splash("you are a cat", "named hops")
music.play(music.createSoundEffect(WaveShape.Sine, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
game.splash("you need to", "reach the treasure")
music.play(music.createSoundEffect(WaveShape.Sine, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
game.splash("the treasure is at", "the end of this level")
music.play(music.createSoundEffect(WaveShape.Sine, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
game.splash("good", "luck!")
music.play(music.createSoundEffect(WaveShape.Sine, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
scene.setBackgroundColor(9)
hops_and_paws = sprites.create(assets.image`cat`, SpriteKind.Player)
controller.moveSprite(hops_and_paws, 100, 0)
tiles.setCurrentTilemap(tilemap`Level`)
hops_and_paws.ay = 350
scene.cameraFollowSprite(hops_and_paws)
