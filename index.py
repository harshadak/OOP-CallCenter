class Call(object):
    def __init__(self, unique_id, caller_name, phone, time, reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.phone = phone
        self.time = time
        self.reason = reason
    
    def display_all(self):
        print "Unique ID:", self.unique_id
        print "Caller Name:", self.caller_name
        print "Caller Phone Number:", self.phone
        print "Time of Call:", self.time
        print "Reason for call:", self.reason
        print "------------------------------"
        return self

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue = len(self.call_list)

    def add_call(self, call_id):
        self.call_list.append(call_id)
        print self.call_list
        print "-------------------"
        return self

    def remove_call(self):
        self.call_list.pop(0)
        print self.call_list
        return self

    def info(self):
        for i in self.call_list:
            print i.caller_name, i.phone
        print "Length of the queue:", len(self.call_list)
        return self
    
    # Ninja Level
    def find_remove(self, phone_num):
        for i in self.call_list:
            if i.phone == phone_num:
                self.call_list.remove(i)
        return self

call1 = Call(1, "John Doe", "123-456-7890", "7:05 am", "Password reset").display_all()
call2 = Call(2, "Mary Doe", "321-654-7790", "7:30 am", "Broken printer").display_all()
call3 = Call(3, "Bella Doe", "333-876-8643", "10:05 am", "Printer ink change").display_all()
call4 = Call(4, "Sam Doe", "564-985-0054", "2:46 pm", "Email sync problem").display_all()
call5 = Call(5, "Jane Doe", "876-541-9854", "8:55 pm", "Blackberry pin not working").display_all()

call_center1 = CallCenter().add_call(call3).add_call(call4).add_call(call1).remove_call().info()
call_center2 = CallCenter().add_call(call2).add_call(call1).add_call(call3).find_remove("333-876-8643").info()
