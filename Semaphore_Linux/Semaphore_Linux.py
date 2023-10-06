import threading
import time
import curses

# create semaphore dot/process
semaphore_1 = threading.Semaphore(0)
semaphore_2 = threading.Semaphore(0)
semaphore_3 = threading.Semaphore(0)
semaphore_4 = threading.Semaphore(0)

# create semaphore process
semaphore_A = threading.Semaphore(0)
semaphore_B = threading.Semaphore(0)
semaphore_C = threading.Semaphore(0)
semaphore_D = threading.Semaphore(0)
semaphore_E = threading.Semaphore(0)
semaphore_F = threading.Semaphore(0)
semaphore_G = threading.Semaphore(0)
semaphore_H = threading.Semaphore(0)
semaphore_I = threading.Semaphore(0)
semaphore_J = threading.Semaphore(0)
semaphore_K = threading.Semaphore(0)

# create interface
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)

# func process
def shooter(target, semaphore_target, semaphore_checkpoint):
    time.sleep(1)  # imitation process
    stdscr.addstr(f"process {target}  passed checkpoing {semaphore_checkpoint}\n")
    stdscr.refresh()
    semaphore_target.release()

# func for dot coordinator
def coordinator(semaphore_checkpoint):
    stdscr.addstr(f"Dot  {semaphore_checkpoint} on\n")
    stdscr.refresh()
    time.sleep(2)
    semaphore_checkpoint.release()

# create flux for process and dot
shooter_A = threading.Thread(target=shooter, args=("A", semaphore_A, semaphore_1))
shooter_B = threading.Thread(target=shooter, args=("B", semaphore_B, semaphore_2))
shooter_C = threading.Thread(target=shooter, args=("C", semaphore_C, semaphore_2))
shooter_J = threading.Thread(target=shooter, args=("J", semaphore_J, semaphore_3))
shooter_I = threading.Thread(target=shooter, args=("I", semaphore_I, semaphore_4))
shooter_D = threading.Thread(target=shooter, args=("D", semaphore_D, semaphore_3))
shooter_E = threading.Thread(target=shooter, args=("E", semaphore_E, semaphore_3))
shooter_F = threading.Thread(target=shooter, args=("F", semaphore_F, semaphore_3))
shooter_G = threading.Thread(target=shooter, args=("G", semaphore_G, semaphore_4))
shooter_H = threading.Thread(target=shooter, args=("H", semaphore_H, semaphore_4))
shooter_K = threading.Thread(target=shooter, args=("K", semaphore_K, semaphore_4))

# create flux for dot
coordinator_1 = threading.Thread(target=coordinator, args=(semaphore_1,))
coordinator_2 = threading.Thread(target=coordinator, args=(semaphore_2,))
coordinator_3 = threading.Thread(target=coordinator, args=(semaphore_3,))
coordinator_4 = threading.Thread(target=coordinator, args=(semaphore_4,))

# func interface
def main(stdscr):
    stdscr.clear()
    stdscr.addstr("press 's' to start or 'q' to exit\n\n")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('s'):
            stdscr.clear()
            stdscr.addstr("programm on\n")
            stdscr.refresh()

            # start process and dot
            shooter_A.start()
            shooter_B.start()
            shooter_C.start()
            shooter_J.start()
            shooter_I.start()
            shooter_D.start()
            shooter_E.start()
            shooter_F.start()
            shooter_G.start()
            shooter_H.start()
            shooter_K.start()

            coordinator_1.start()
            coordinator_2.start()
            coordinator_3.start()
            coordinator_4.start()

            stdscr.addstr("press 'q' for exit\n")
            stdscr.refresh()
        
    stdscr.addstr("wait ended process\n")
    stdscr.refresh()

    # wait ended all flux
    shooter_A.join()
    shooter_B.join()
    shooter_C.join()
    shooter_J.join()
    shooter_I.join()
    shooter_D.join()
    shooter_E.join()
    shooter_F.join()
    shooter_G.join()
    shooter_H.join()
    shooter_K.join()
    coordinator_1.join()
    coordinator_2.join()
    coordinator_3.join()
    coordinator_4.join()

    stdscr.addstr("all process are completed.\n Press any button for exit.\n")
    stdscr.refresh()
    stdscr.getch()

# main while curses
curses.wrapper(main)
