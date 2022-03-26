   size = os.stat(file_name).st_size
    async with aiofiles.open(file_name, mode='rb') as fs:
        a = ijson.items(fs, 'results.bindings.item')
        async for o in a:
            yield o, fs.tell(), size