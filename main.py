from asyncio import get_event_loop


async def run_eval(vle):
    print(vle)


def run_in_func():
    prompt = 'new message to run nah'
    globals()["prompt"] = prompt
    code = "await run_eval(prompt)"
    loop = get_event_loop()
    loop.run_until_complete(aexec(code))

async def aexec(code):
    # Make an async function with the code and `exec` it
    exec(
        f'async def __ex(): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )

    # Get `__ex` from local variables, call it and return the result
    return await locals()['__ex']()

if __name__ == "__main__":
    run_in_func()
