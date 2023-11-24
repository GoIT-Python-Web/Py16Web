from time import sleep


def convert_image(filename, target_format):
    print(f"Converting {filename} to {target_format} ...")
    sleep(0.5)
    return f"{filename.split('.')[0]}.{target_format}"
