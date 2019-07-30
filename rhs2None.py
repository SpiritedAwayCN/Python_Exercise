#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

s = '''\
### START CODE HERE ### 
    
    # Create the placeholders for "logits" (z) and "labels" (y) (approx. 2 lines)
    z = tf.placeholder(tf.float32, name="z")
    y = tf.placeholder(tf.float32, name="y")
    
    # Use the loss function (approx. 1 line)
    cost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
    
    # Create a session (approx. 1 line). See method 1 above.
    sess = tf.Session()
    
    # Run the session (approx. 1 line).
    cost = sess.run(cost, feed_dict={z: logits, y: labels})
    
    # Close the session (approx. 1 line). See method 1 above.
    sess.close()
    
    ### END CODE HERE ###
    
    return cost\
'''

# uncomment this line for multi-fragment case
# s = '\n\n'.join([ s for _ in range(2) ])

reCode = re.compile(r'### START CODE HERE ###(.*?)### END CODE HERE ###', re.S)
reAssign = re.compile(r'^(\s*.*?\s*=\s*)(.*)(\s*)$', re.M)

hrs2None = lambda mat: reAssign.sub(r'\g<1>None\g<3>', mat.group(0))

res = reCode.sub(hrs2None, s)
print(res)