(in-package :blackboard_demo)

(defparameter *object-space* (make-space-instance '(object-space)))

(translate-unit-class gazebo_plugins-msg:<WorldState>)

(define-unit-class position-3d ()
  (x y z 
   (objects-at
    :link (object location)))
  (:dimensional-values 
   (x :point x)
   (y :point y)
   (z :point z)))

(define-unit-class object ()
  (name 
   color shape
   (location 
    :link (position-3d objects-at)
    :singular t)))
  