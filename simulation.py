import sqlite3
import queue
import re



def browse_data(): #retrieves the tasks from database test2.db.
    conn = sqlite3.connect("test2.db")
    cursor = conn.cursor()
    sql_st = ("SELECT id, arrival, duration FROM stuffToPlot ORDER BY arrival ASC") #selecting tasks from the database, inside the stuffToPlot table, taking them as a list of tuples, ordered by shortest to longest arrival time.
    cursor.execute(sql_st)
    records = cursor.fetchall() #retrieves all tasks in a list of tuples.


    for i in records: #loops through the list of tuples and inserts them into a queue.
        dataset_queue.put(i)

    conn.commit()
    conn.close()
    return dataset_queue #returns the queue with tasks.


dataset_queue = queue.Queue() #initialises an empty queue.

def processing(): #processing tasks entering the system, checking their id validation and assignment to processors with completion times.

    #processors start with 0 time.
    processor1 = 0
    processor2 = 0
    processor3 = 0

    time = [] #A LIST, COLLECTING ALL SYSTEMS EVENTS, TO BE CHRONOLOGICALLY SORTED AT THE END OF SIMULATION.

    queue = browse_data() #calling the method to retrieve the queue with 100 tasks.
    for item in range(queue.qsize()): #looping through the queue's length.
        item = queue.get() #taking the task out from the queue.

        #appending the status statement of the entering task as a tuple to the time list. The first tuple's item - Task's arrival time is used as a refrence for sorting.
        time.append((item[1],f"\n**  [{item[1]}] : Task [{item[0]}] with duration {item[2]} enters the system."))

        #checking task's id if it contains at least three different type character's in order to have the id accepted.
        uppercase = re.search("[A-Z]",item[0])
        lowercase = re.search("[a-z]",item[0])
        digits = re.search("[\d]",item[0])
        special = re.search("[-@#*&_]",item[0])

        #if the id contains the specified charachter type, update the accepted_score.
        accepted_score = 0
        if uppercase:
            accepted_score += 1
        if lowercase:
            accepted_score += 1
        if digits:
            accepted_score += 1
        if special:
            accepted_score += 1
        if  accepted_score >= 3:

            #if the accepted_score reaches >= 3, task accepted status statement is appended to the time list, task's arrival time, used as sorting refrence.
            #alternatively task will be deemed 'unfeasible and discarded' as per line 148.
            time.append((item[1],f"\n** Task [{item[0]}] accepted."))

            #UPDATING THE PROCESSORS#

# ############################### PROCESSOR 1 ##########################################
            if item[1]> processor1: #if task's arrival time is bigger than processor1 time:

                #appending the current task's 'assignment to processor1' status statement to time list. Tasks arrival time used as assignment time to processor1.
                time.append((item[1],f"\n** [{item[1]}] : Task [{item[0]}] assigned to a proccesor [#1]. "))

                #processor 1 becomes preoccupied from current task's arrival time until task's duration ends.
                processor1 = item[1]+item[2]

                #task's completion status statement is appended inside the time list, arrival+duration time used as sorting reference.
                time.append((item[1]+item[2],f"\n**  [{item[1]+item[2]}] : Task [{item[0]}] completed."))

            ############ TASK ON HOLD - PROCESSOR 1 FINISHES FIRST #############

            #if the task's arrival is lesser than processor1 and processor1 will finish its assigned task quicker than other processors:
            elif item[1] < processor1 and processor1 <= processor2 and processor1 <= processor3:

                #then place the newly arrived task on hold, append its status statement to time list, task's arrival time used as sorting reference.
                time.append((item[1],f"\n** Task [{item[0]}] on hold"))

                #the task gets assigned to processor1, same time as processor1 completes the previous task, therefore current task's arrival == previous task's completion time.
                time.append((processor1,f"\n** [{processor1}] : Task [{item[0]}] assigned to a proccesor [#1]. "))

                #the current task's completion time will be equal to: previous task's completion time + current task's duration time.
                time.append((processor1 + item[2], f"\n**  [{processor1 + item[2]}] : Task [{item[0]}] completed."))
                processor1 += item[2]

# # ############################# PROCESSOR 2 ##########################################
            elif item[1]> processor2: #if task's arrival time is lesser than processor1, but bigger than processor2's time:

                #Same action as line 67, appending task's 'assignment to processor2' status statement to time list.
                time.append((item[1],f"\n** [{item[1]}] : Task [{item[0]}] assigned to a proccesor [#2]. "))

                #Same action as line 71, now processor2 becomes preoccupied from current task's arrival time until task's duration ends.
                processor2 = item[1]+item[2]

                #Same action as line 73
                time.append((item[1]+item[2],f"\n**  [{item[1] + item[2]}] : Task [{item[0]}] completed."))

            ############ TASK ON HOLD - PROCESSOR 2 FINISHES FIRST #############

            #if the task's arrival is lesser than processor1 and processor2, while processor2 will finish its assigned task quicker than other processors:
            elif item[1] < processor2 and processor2 < processor1 and processor2 <= processor3:

                #then Same action as line 82.
                time.append((item[1],f"\n** Task [{item[0]}] on hold"))

                #Same action as line 84, task assigned to processor2, same time as processor2 completes the previous task.
                time.append((processor2,f"\n** [{processor2}] : Task [{item[0]}] assigned to a proccesor [#2]. "))

                #Same action as line 87
                time.append((processor2 + item[2], f"\n**  [{processor2 + item[2]}] : Task [{item[0]}] completed."))
                processor2 += item[2]

# # # ############################# PROCESSOR 3 ##########################################
            elif item[1]> processor3: #if task's arrival time is lesser than processor1 and processor2, but bigger than processor3's time:

                #Same action as line 67, appending task's 'assignment to processor3' status statement to time list.
                time.append((item[1],f"\n** [{item[1]}] : Task [{item[0]}] assigned to a proccesor [#3]. "))

                #Same action as line 71, now processor3 becomes preoccupied from current task's arrival time until task's duration ends.
                processor3 = item[1]+item[2]

                #Same action as line 73
                time.append((item[1]+item[2],f"\n**  [{item[1]+item[2]}] : Task [{item[0]}] completed."))

            ############ TASK ON HOLD - PROCESSOR 3 FINISHES FIRST #############

            #if the task's arrival is lesser than all 3 processors, while processor3 will finish its assigned task quicker than other processors:
            elif item[1] < processor3 and processor3 < processor1 and processor3 < processor2:

                #then Same action as line 82.
                time.append((item[1],f"\n** Task [{item[0]}] on hold"))

                #Same action as line 84, task assigned to processor3, same time as processor3 completes the previous task.
                time.append((processor3,f"\n** [{processor3}] : Task [{item[0]}] assigned to a proccesor [#3]. "))

                #Same action as line 87
                time.append((processor3 + item[2], f"\n**  [{processor3 + item[2]}] : Task [{item[0]}] completed."))
                processor3 += item[2]

        #If task's id is not acceptable, then task is recorded as unfeasible and appended to time list. Task's arrival time is used as a sorting refrence.
        else:
             time.append((item[1],f"\n** Task: [{item[0]}] unfeasible and discarded."))

        #### CHRONOLOGICALLY SORTING SIMULATION'S EVENTS ####
        time.sort()

        ######## REMOVING THE FIRST TUPLE'S ITEM USED TO CREATE CHRONOLOGICAL ORDER ########
        new_list = [x[1] for x in time]

        ##### CREATING A LIST TO ACCESS SIMULATION'S COMPLETION TIME #####
        completion = [x[0] for x in time]

        #PRINTING OUT THE SIMULATION
    return print(*new_list, sep='\n'), print(f"\n** [{completion[-1]}] : SIMULATION COMPLETED. **")


if __name__ == "__main__":
    processing() #calling the reusable processing function.
