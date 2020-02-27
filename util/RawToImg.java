
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import javax.imageio.ImageIO;

public class RawToImg {
    int width;
    int height;
    BufferedImage img;

    public RawToImg(){
    }
    public void load(String path) throws Exception {
        FileReader fr = new FileReader(new File(path));
        BufferedReader br = new BufferedReader(fr);

        String line = br.readLine();
        String[] dat;
        dat = line.split(",");
        width = Integer.parseInt(dat[0]);
        height = Integer.parseInt(dat[1]);

        img = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

        int col = 0;
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                //System.out.println("Doing "+x+","+y);
                line = br.readLine();
                dat = line.split(",");

                col = (int) (Float.parseFloat(dat[0]) * 255) << 24;
                col += (int) (Float.parseFloat(dat[1]) * 255) << 16;
                col += (int) (Float.parseFloat(dat[2]) * 255) << 8;
                col += (int) (Float.parseFloat(dat[3]) * 255);

                img.setRGB(x, y, col);
            }
        }
        br.close();
    }

    public void save(String path) throws Exception{
        ImageIO.write(img, "png", new File(path));
    }

    public static void main(String args[]) {
        RawToImg inst = new RawToImg();
        try {
            inst.load(args[0]);
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            inst.save(args[1]);
        } catch(Exception e) {
            e.printStackTrace();
        }    
        System.out.println("DONE");
    }
}
