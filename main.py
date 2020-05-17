from canvasapi import Canvas
import pstats
import tkinter
from pstats import SortKey
import cProfile


from PeerReviewerClass import peerReviewer

# window = tkinter.Tk()
# frame = tkinter.Frame(window, bg = "green")
# frame.pack()
#
# window.mainloop()

# Canvas API URL
API_URL = "https://canvas.ucdavis.edu"
# Canvas API key
API_KEY = "3438~1dZ0nJfFzMLFk4dJxn6RU4KMgSiQ7tmZTpqqMEwrelzHqx9XiD5tDJDFlIABeFbg"
canvas = Canvas(API_URL, API_KEY)

# window = Tk
# window.title = "new"



# data = {
#     241893 : {'posted_grade': 0.5},
#     241892 : {'posted_grade': 0.75}
# }
#
# assignment = canvas.get_course(1599).get_assignment(467392)
# assignment.submissions_bulk_update(grade_data = data)
#





a = cProfile.run('peerReviewer(canvas, canvas.get_current_user())', 'peerreviewer_stats')
p = pstats.Stats('peerreviewer_stats')
p.sort_stats(SortKey.TIME).print_stats(10)

# a = view_Courses(canvas,canvas.get_current_user())
# b = view_assignments(canvas,canvas.get_current_user(),a.course_id)
# c = view_peer_reviews(canvas,canvas.get_current_user(),a.course_id,b.current_assignment_id)

# student_A = student(canvas,241892,1599,348537)
# thelist = student_A.get_peer_reviews_assigned()
pass



