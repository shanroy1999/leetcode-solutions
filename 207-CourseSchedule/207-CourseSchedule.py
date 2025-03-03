class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Track the course and its prerequisites
        preMap = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)           # Append the prereq to the list for each course      
        visitSet = set()    # to track the graph cycle of course and prerequisite

        def dfs(course):
            # if the course is already in the visitSet => encountered it again
            # cycle detected => cannot be completed => return False
            if course in visitSet:
                return False
            # if there is no prerequisite required for a course 
            # course can be completed => return True
            if preMap[course] == []:
                return True
            # Mark the course as we are visiting
            visitSet.add(course)
            # Loop through the prerequisite of the course and run DFS on each
            # If any of the course => cannot be completed => return False
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            # Remove the course from the visitSet as we finished visiting the course
            visitSet.remove(course)
            # Course can be visited => prereq can be set to empty list
            # return True immediately => repetition not required
            preMap[course] = []
            return True

        # interate through each course in numCourses => graph may not be fully connected
        for course in range(numCourses):
            # Call dfs on every single course
            # if any dfs return false => return false immediately
            if not dfs(course):
                return False
        return True

