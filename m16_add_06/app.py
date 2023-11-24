from service_convert_image import convert_image
from priority_queue import PriorityQueue


def main():
    pq = PriorityQueue()

    pq.enqueue(('image.jpg', 'png'), 1)
    pq.enqueue(('image1.jpg', 'png'), 1)
    pq.enqueue(('image2.jpg', 'png'), 1)
    pq.enqueue(('student.jpg', 'png'), 3)
    pq.enqueue(('anime.bmp', 'webp'), 10)
    pq.enqueue(('image10.jpg', 'png'), 1)
    pq.enqueue(('image20.jpg', 'png'), 1)
    pq.enqueue(('work.png', 'jpg'), 5)

    while not pq.is_empty():
        task = pq.dequeue()
        result = convert_image(*task)
        print(f"Успішно виконано завдання {result}")


if __name__ == '__main__':
    main()

