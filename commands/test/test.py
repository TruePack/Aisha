from aisha import Aisha

aisha = Aisha()


@aisha.command(name='test')
async def test(ctx):
    await ctx.send("govn")

