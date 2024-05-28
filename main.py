from asyncio import get_event_loop


async def run_eval(vle):
    print(vle)


async def aexec(code):
    # Make an async function with the code and `exec` it
    exec(
        f'async def __ex(): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )

    # Get `__ex` from local variables, call it and return the result
    return await locals()['__ex']()


if __name__ == "__main__":
    prompt = 'new message to run'
    code = "await run_eval(prompt)"
    loop = get_event_loop()
    loop.run_until_complete(aexec(code))
