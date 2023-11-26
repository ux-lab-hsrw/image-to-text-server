from image_handler import handle_image, init as init_image_handler

init_image_handler()

results = handle_image("image_test.jpg")

print(results)