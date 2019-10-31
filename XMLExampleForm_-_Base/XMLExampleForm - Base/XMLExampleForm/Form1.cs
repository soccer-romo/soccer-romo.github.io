using System;
using System.Xml;  //Xml library
using System.Windows.Forms;



namespace XMLExampleForm
{
    public partial class Form1 : Form
    {
        int idx;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            XmlReader reader = XmlReader.Create("Student List.xml");
            Student myStudent = new Student();

            while (reader.Read())
            {
                if(reader.IsStartElement())
                {
                    switch(reader.Name)
                    {
                        case "Student":
                            if (myStudent.FName != null)
                            {
                                lstStudents.Items.Add(myStudent);
                                myStudent = new Student();
                            }
                            break;
                        case "FName":           //found FName taf
                            reader.Read();      //Read again to get value
                            myStudent.FName = reader.Value;
                            break;
                        case "LName":
                            reader.Read();
                            myStudent.LName = reader.Value;
                            break;
                        case "Major":
                            reader.Read();
                            myStudent.Major = reader.Value;
                            break;
                        case "Gpa":
                            reader.Read();
                            myStudent.Gpa = float.Parse(reader.Value);
                            break;

                    }
                }
            }
            if (myStudent.FName != null)
            {
                lstStudents.Items.Add(myStudent);
                myStudent = new Student();
            }
        }  // end of method

        private void lstStudents_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (lstStudents.SelectedIndex != -1)
            {
                idx = lstStudents.SelectedIndex;

                Student aStudent = (Student)lstStudents.Items[idx];

                txtBxFName.Text = aStudent.FName;
                txtBxLName.Text = aStudent.LName;
                txtBxMajor.Text = aStudent.Major;
                txtBxGpa.Text = aStudent.Gpa.ToString();
            }
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            Student aStudent = new Student(txtBxFName.Text,
                                           txtBxLName.Text,
                                           txtBxMajor.Text,
                                           float.Parse(txtBxGpa.Text));
            lstStudents.Items[idx] = aStudent;

            using (XmlWriter writer = XmlWriter.Create("Student List.xmlupd"))
            {
                foreach (Student item in lstStudents.Items)
                {
                    writer.WriteStartAttribute("Student");
                    writer.WriteStartAttribute("FName",item.FName);
                    writer.WriteStartAttribute("LName",item.LName);
                    writer.WriteStartAttribute("Major", item.Major);
                    writer.WriteStartAttribute("Gpa",item.Gpa.ToString());
                    writer.WriteEndAttribute();


                }
            }
        }
       
    }
}
