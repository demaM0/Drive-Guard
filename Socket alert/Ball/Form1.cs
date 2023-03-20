using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Globalization;
using System.Media;
namespace Ball
{
    public partial class Form1 : Form
    {
        Timer TT = new Timer();
        public int port;
        public string message;
        public int byteCount;
        public NetworkStream stream;
        public byte[] sendData;
        public TcpClient tcpClient;
        Bitmap off;
        float alarm;
        SoundPlayer SoundPlayer = new SoundPlayer("alarm.wav");
        public Form1()
        {
            InitializeComponent();
            this.WindowState = FormWindowState.Maximized;
            this.Paint += Form1_Paint;
            TT.Tick += TT_Tick;
            TT.Start();
        }
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            DrawDubble(e.Graphics);
        }
        private void TT_Tick(object sender, EventArgs e)
        {
            byte[] receiveBuffer = new byte[1024];
            int bytesReceived = stream.Read(receiveBuffer, 0, receiveBuffer.Length);
            string data = Encoding.UTF8.GetString(receiveBuffer, 0, bytesReceived);
            string[] d = data.Split(',');
            //if (d.Length == 2)
            {
                if (float.TryParse(d[0], NumberStyles.Any, CultureInfo.InvariantCulture, out alarm))
                {
                    if (alarm == 1)
                    {
                        MessageBox.Show("Alert");
                        //SoundPlayer.Play();
                    }
                }
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            off = new Bitmap(this.ClientSize.Width, this.ClientSize.Height);
            String hostName = System.Net.Dns.GetHostName();
            tcpClient = new TcpClient(hostName, 8000);
            stream = tcpClient.GetStream();
        }
        void DrawScene(Graphics g)
        {
            g.Clear(Color.LightBlue);
            
            //g.FillEllipse(Brushes.Black, CX, CY, 45, 45);
        }
        void DrawDubble(Graphics g)
        {
            Graphics g2 = Graphics.FromImage(off);
            DrawScene(g2);
            g.DrawImage(off, 0, 0);
        }
    }
}
