import canvasapi
from canvasapi import Canvas



class peer_review:
    def __init__(self,canvas : Canvas, course_id, submission: canvasapi.submission, assessor_id):
        self.submission = submission
        self.submission_id = submission.id
        self.assessor_id = assessor_id
        self.user_id = submission.user_id
        self.assignment_id = submission.assignment_id
        self.course = canvas.get_course(course_id)
        self.work_flow = self.get_work_flow()
        self.rubric = self.get_rubric()
        self.given_score = self.get_score()
        pass


    def get_work_flow(self):
        reviews = self.course.get_assignment(self.assignment_id).get_peer_reviews()
        for review in reviews:
            if review.assessor_id == self.assessor_id :
                if review.user_id == self.user_id :
                    return review.workflow_state


    def get_score(self):
        assessments = self.rubric.assessments
        reviews = self.course.get_assignment(self.assignment_id).get_peer_reviews()
        submissions = self.course.get_assignment(self.assignment_id).get_submissions()
        for review in reviews:
                    for assessment in assessments:
                        if self.assessor_id == (assessment['assessor_id']):
                            for submission in submissions:
                                if submission.id == review.asset_id:
                                    return assessment['score']



    def get_rubric(self):
        rubric = self.course.get_rubrics(rubric_association_id=self.assignment_id, include=["peer_assessments"], style="full")[0]
        rubric_id = rubric.id
        rubric = self.course.get_rubric(rubric_id, include=["peer_assessments"], style="full")
        return rubric


class student:
    def __init__(self,canvas : Canvas, user_id, course_id, assignment_id):
        self.canvas = canvas
        self.id = user_id
        self.course_id = course_id
        self.course = canvas.get_course(course_id)
        self.assignment_id = assignment_id
        self.peer_reviews_completed = 0
        self.number_of_reviews_assigned = 0
        self.peer_reviews = self.get_peer_reviews_assigned()

        # self.name = canvas.get_user(user_id).name


    def get_peer_reviews_assigned(self):
        peer_reviews_assigned = []
        reviews = self.course.get_assignment(self.assignment_id).get_peer_reviews()
        for review in reviews :
            if review.assessor_id == self.id:
                submission = self.course.get_assignment(self.assignment_id).get_submission(review.user_id)
                peer_reviews_assigned.append(peer_review(self.canvas,self.course_id,submission,self.id))
                if review.workflow_state == 'completed' :
                    self.peer_reviews_completed = self.peer_reviews_completed +1

        self.number_of_reviews_assigned = len(peer_reviews_assigned)
        return peer_reviews_assigned




