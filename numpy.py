import numpy

# Uztaisa objektu, ar kuru var viegli darīt matemātiskas darbības.
print(numpy.array([1, 2, 3]))
#[1 2 3]

# Saskaita divu numpy.array objektu elementus
print(numpy.add(numpy.array([1, 2, 3]),numpy.array([1, 2, 3])))
#[2 4 6]
# var arī izmantot +
print(numpy.array([1, 2, 3]) + numpy.array([1, 2, 3]))
