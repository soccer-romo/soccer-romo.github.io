namespace XMLExampleForm
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lstStudents = new System.Windows.Forms.ListBox();
            this.lblMessage = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.txtBxFName = new System.Windows.Forms.TextBox();
            this.txtBxLName = new System.Windows.Forms.TextBox();
            this.txtBxMajor = new System.Windows.Forms.TextBox();
            this.txtBxGpa = new System.Windows.Forms.TextBox();
            this.btnUpdate = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lstStudents
            // 
            this.lstStudents.FormattingEnabled = true;
            this.lstStudents.ItemHeight = 18;
            this.lstStudents.Location = new System.Drawing.Point(35, 61);
            this.lstStudents.Name = "lstStudents";
            this.lstStudents.Size = new System.Drawing.Size(211, 238);
            this.lstStudents.TabIndex = 0;
            this.lstStudents.SelectedIndexChanged += new System.EventHandler(this.lstStudents_SelectedIndexChanged);
            // 
            // lblMessage
            // 
            this.lblMessage.AutoSize = true;
            this.lblMessage.Location = new System.Drawing.Point(3, 339);
            this.lblMessage.Name = "lblMessage";
            this.lblMessage.Size = new System.Drawing.Size(226, 18);
            this.lblMessage.TabIndex = 1;
            this.lblMessage.Text = "Welcome to XML Student Maint";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(354, 77);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(85, 18);
            this.label1.TabIndex = 2;
            this.label1.Text = "First Name";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(474, 77);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(84, 18);
            this.label2.TabIndex = 3;
            this.label2.Text = "Last Name";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(354, 147);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 18);
            this.label3.TabIndex = 4;
            this.label3.Text = "Major";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(474, 147);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(41, 18);
            this.label4.TabIndex = 5;
            this.label4.Text = "GPA";
            // 
            // txtBxFName
            // 
            this.txtBxFName.Location = new System.Drawing.Point(357, 110);
            this.txtBxFName.Name = "txtBxFName";
            this.txtBxFName.Size = new System.Drawing.Size(109, 26);
            this.txtBxFName.TabIndex = 6;
            // 
            // txtBxLName
            // 
            this.txtBxLName.Location = new System.Drawing.Point(479, 110);
            this.txtBxLName.Name = "txtBxLName";
            this.txtBxLName.Size = new System.Drawing.Size(124, 26);
            this.txtBxLName.TabIndex = 7;
            // 
            // txtBxMajor
            // 
            this.txtBxMajor.Location = new System.Drawing.Point(360, 176);
            this.txtBxMajor.Name = "txtBxMajor";
            this.txtBxMajor.Size = new System.Drawing.Size(79, 26);
            this.txtBxMajor.TabIndex = 8;
            // 
            // txtBxGpa
            // 
            this.txtBxGpa.Location = new System.Drawing.Point(481, 176);
            this.txtBxGpa.Name = "txtBxGpa";
            this.txtBxGpa.Size = new System.Drawing.Size(97, 26);
            this.txtBxGpa.TabIndex = 9;
            // 
            // btnUpdate
            // 
            this.btnUpdate.BackColor = System.Drawing.Color.LightSeaGreen;
            this.btnUpdate.Location = new System.Drawing.Point(436, 243);
            this.btnUpdate.Name = "btnUpdate";
            this.btnUpdate.Size = new System.Drawing.Size(79, 45);
            this.btnUpdate.TabIndex = 10;
            this.btnUpdate.Text = "Update";
            this.btnUpdate.UseVisualStyleBackColor = false;
            this.btnUpdate.Click += new System.EventHandler(this.btnUpdate_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.LightSeaGreen;
            this.ClientSize = new System.Drawing.Size(894, 362);
            this.Controls.Add(this.btnUpdate);
            this.Controls.Add(this.txtBxGpa);
            this.Controls.Add(this.txtBxMajor);
            this.Controls.Add(this.txtBxLName);
            this.Controls.Add(this.txtBxFName);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblMessage);
            this.Controls.Add(this.lstStudents);
            this.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "XML Student Info";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox lstStudents;
        private System.Windows.Forms.Label lblMessage;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtBxFName;
        private System.Windows.Forms.TextBox txtBxLName;
        private System.Windows.Forms.TextBox txtBxMajor;
        private System.Windows.Forms.TextBox txtBxGpa;
        private System.Windows.Forms.Button btnUpdate;
    }
}

