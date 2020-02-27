
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import javax.imageio.ImageIO;

public class RawToImg {
    int width;
    int height;

    public RawToImg(String args[]) throws Exception {
        if (args.length < 2) {
            throw new Exception("Insufficient args");
        }

        FileReader fr = new FileReader(new File(args[0]));
        BufferedReader br = new BufferedReader(fr);

        String line = br.readLine();
        String[] dat;
        dat = line.split(",");
        width = Integer.parseInt(dat[0]);
        height = Integer.parseInt(dat[1]);

        BufferedImage img = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

        int col = 0;
        for (int y = 0; y < width; y++) {
            for (int x = 0; x < width; x++) {
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

        ImageIO.write(img, "png", new File(args[1]));
    }

    public static void main(String args[]) {
        try {
            new RawToImg(args);
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("DONE");
    }
}
