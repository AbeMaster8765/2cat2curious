namespace SpriteKind {
    export const Coin = SpriteKind.create()
    export const Flower = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Coin, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    sprites.destroy(otherSprite)
})
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
sprites.onOverlap(SpriteKind.Player, SpriteKind.Flower, function (sprite, otherSprite) {
    Bee = sprites.create(img`
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
        `, SpriteKind.Enemy)
    animation.runImageAnimation(
    Bee,
    assets.animation`Bee`,
    100,
    false
    )
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`chest`, function (sprite, location) {
    game.setGameOverEffect(true, effects.confetti)
    game.gameOver(true)
})
let Bee: Sprite = null
let Flower: Sprite = null
let Coin: Sprite = null
let hops_and_paws: Sprite = null
scene.setBackgroundColor(9)
hops_and_paws = sprites.create(assets.image`cat`, SpriteKind.Player)
controller.moveSprite(hops_and_paws, 100, 0)
tiles.setCurrentTilemap(tilemap`Level`)
hops_and_paws.ay = 350
scene.cameraFollowSprite(hops_and_paws)
for (let value of tiles.getTilesByType(assets.tile`Coin`)) {
    Coin = sprites.create(assets.image`Coin`, SpriteKind.Coin)
    animation.runImageAnimation(
    Coin,
    assets.animation`CoinSpin`,
    100,
    true
    )
    tiles.placeOnTile(Coin, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
}
for (let value of tiles.getTilesByType(assets.tile`FlowerPLACEHOLDER`)) {
    Flower = sprites.create(assets.image`Flower`, SpriteKind.Flower)
    tiles.placeOnTile(Flower, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
}
