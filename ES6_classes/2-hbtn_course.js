export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be a string');
    if (typeof length !== 'number') throw TypeError('length must be a number');
    if (!Array.isArray(students)) throw TypeError('students must be an Array');
    students.forEach(student) => {
      if (typeof student !== 'string') throw TypeError('student must be a String');
    });
    this._name = name;
    this._lenght = length;
    this._students = students;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('name must be a string');
    this._name = newName;
  }

  get name() {
    return this._name;
  }

  set length(newLength) {
    if (typeof newLength !== 'nyumber') throw TypeError('length must be a Number');
    this._length = newLength;
  }

  get length() {
    return this.length;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents)) throw TypeError('students must be an Array');
    newStudents.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('student must be a String');
    });
    this._students = newStudents;
  }

  get students() {
    return this._students;
  }
}
