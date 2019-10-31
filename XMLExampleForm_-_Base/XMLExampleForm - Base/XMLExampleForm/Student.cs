using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace XMLExampleForm
{
    class Student
    {
        #region data fields
        private string fName;
        private string lName;
        private string major;
        private float gpa;


        #endregion
        #region public properties
        public string FName { get => fName; set => fName = value; }
        public string LName { get => lName; set => lName = value; }
        public string Major { get => major; set => major = value; }
        public float Gpa { get => gpa; set => gpa = value; }
        #endregion
        #region constructors
        public Student(string fName, string lName, string major, float gpa)
        {
            this.fName = fName;
            this.lName = lName;
            this.major = major;
            this.gpa = gpa;
        }
        public Student() { }
        #endregion
        #region methods
        public override string ToString()
        {
            return FName + "," + lName + "," + major + "," + gpa.ToString();
        }
        #endregion
    }
}
