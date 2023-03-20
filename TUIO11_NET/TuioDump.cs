using System;
using TUIO;

	public class TuioDump : TuioListener
	{

		public void addTuioObject(TuioObject tobj) {
			Console.WriteLine("add obj "+tobj.SymbolID+" "+tobj.SessionID+" "+tobj.X+" "+tobj.Y+" "+tobj.Angle);
		}

		public void updateTuioObject(TuioObject tobj) {
			Console.WriteLine("set obj "+tobj.SymbolID+" "+tobj.SessionID+" "+tobj.X+" "+tobj.Y+" "+tobj.Angle+" "+tobj.MotionSpeed+" "+tobj.RotationSpeed+" "+tobj.MotionAccel+" "+tobj.RotationAccel);
		}

		public void removeTuioObject(TuioObject tobj) {
			Console.WriteLine("del obj "+tobj.SymbolID+" "+tobj.SessionID);
		}

		public void addTuioCursor(TuioCursor tcur) {
			Console.WriteLine("add cur "+tcur.CursorID + " ("+tcur.SessionID+") "+tcur.X+" "+tcur.Y);
		}

		public void updateTuioCursor(TuioCursor tcur) {
			Console.WriteLine("set cur "+tcur.CursorID + " ("+tcur.SessionID+") "+tcur.X+" "+tcur.Y+" "+tcur.MotionSpeed+" "+tcur.MotionAccel);
		}

		public void removeTuioCursor(TuioCursor tcur) {
			Console.WriteLine("del cur "+tcur.CursorID + " ("+tcur.SessionID+")");
		}

		public void addTuioBlob(TuioBlob tblb) {
			Console.WriteLine("add blb "+tblb.BlobID + " ("+tblb.SessionID+") "+tblb.X+" "+tblb.Y+" "+tblb.Angle+" "+tblb.Width+" "+tblb.Height+" "+tblb.Area);
		}

		public void updateTuioBlob(TuioBlob tblb) {
			Console.WriteLine("set blb "+tblb.BlobID + " ("+tblb.SessionID+") "+tblb.X+" "+tblb.Y+" "+tblb.Angle+" "+tblb.Width+" "+tblb.Height+" "+tblb.Area+" "+tblb.MotionSpeed+" "+tblb.RotationSpeed+" "+tblb.MotionAccel+" "+tblb.RotationAccel);
		}

		public void removeTuioBlob(TuioBlob tblb) {
			Console.WriteLine("del blb "+tblb.BlobID + " ("+tblb.SessionID+")");
		}

		public void refresh(TuioTime frameTime) {
		}

		public static void Main(String[] argv) {
			TuioDump demo = new TuioDump();
			TuioClient client = null;

			switch (argv.Length) {
				case 1:
					int port = 0;
					port = int.Parse(argv[0],null);
					if(port>0) client = new TuioClient(port);
					break;
				case 0:
					client = new TuioClient();
					break;
			}

			if (client!=null) {
				client.addTuioListener(demo);
				client.connect();
				Console.WriteLine("listening to TUIO messages at port " + client.getPort());

			} else Console.WriteLine("usage: java TuioDump [port]");
		}
	}
