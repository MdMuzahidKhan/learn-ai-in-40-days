# Approach: Use a queue so print jobs are processed in the same order they were added.

from queue import Queue


def process_print_jobs():
    printer_queue = Queue()

    printer_queue.enqueue("Document1.pdf")
    printer_queue.enqueue("Image.png")
    printer_queue.enqueue("Report.docx")

    print("Jobs added to queue.")
    print("First job in queue:", printer_queue.peek())
    print()

    while not printer_queue.is_empty():
        current_job = printer_queue.dequeue()
        print("Printing:", current_job)

    print()
    print("All print jobs completed.")


process_print_jobs()