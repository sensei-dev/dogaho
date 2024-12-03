using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp4
{
    public partial class Form1 : Form
    {
        public class Konyv
        {
            public string Author { get; set; }
            public string Title { get; set; }
            public int Price { get; set; }
            public Konyv(string author, string title, int price)
            {
                Author = author;
                Title = title;
                Price = price;
            }
            public static void infoBook()
            { }
            public static void deleteBook()
            { }
            public static void addBook()
            { }
        }
        public List<Konyv> konyvList;
        public Form1()
        {
            konyvList = new List<Konyv>();
            InitializeComponent();
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string author = textBox1.Text;
            string title = textBox2.Text;
            int price = 0;
            string price_ = textBox3.Text;
            if (author == "" || title == "" || price_ == "")
            {
                MessageBox.Show("Az összes mező kötelező!");
                return;
            }

            try
            {
                price = int.Parse(price_);
            }
            catch
            {
                MessageBox.Show("Rossz értéket adott meg!");
                return;
            }

            konyvList.Add(new Konyv(author, title, price));

            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

            //konyvList.Add(new Konyv(author, title, price));

            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            checkBox2.Checked = false;
            checkBox3.Checked = false;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            checkBox3.Checked = false;
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            checkBox2.Checked = false;
        }
    }
}
