using System;
using System.Drawing;
using TUIO;

	public class TuioDemoObject : TuioObject
	{

		SolidBrush black = new SolidBrush(Color.Black);
		SolidBrush white = new SolidBrush(Color.White);

		public TuioDemoObject (TuioObject o) : base(o) {
		}

		public void paint(Graphics g) {

			int Xpos = (int)(xpos*TuioDemo.width);
			int Ypos = (int)(ypos*TuioDemo.height);
			int size = TuioDemo.height/10;

			g.TranslateTransform(Xpos,Ypos);
			g.RotateTransform((float)(angle/Math.PI*180.0f));
			g.TranslateTransform(-1*Xpos,-1*Ypos);

			g.FillRectangle(black, new Rectangle(Xpos-size/2,Ypos-size/2,size,size));

			g.TranslateTransform(Xpos,Ypos);
			g.RotateTransform(-1*(float)(angle/Math.PI*180.0f));
			g.TranslateTransform(-1*Xpos,-1*Ypos);

			Font font = new Font("Arial", 10.0f);
			g.DrawString(symbol_id+"",font, white, new PointF(Xpos-10,Ypos-10));
		}

	}
