
import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.function.Consumer;

import javax.imageio.ImageIO;

class ImgToRaw {
    BufferedImage img;
    int mode;
    boolean alpha;

    public ImgToRaw(String args[]) throws Exception {
        if (args.length < 2) {
            throw new Exception("Insufficient args");
        }

        mode = args.length > 2 ? Integer.parseInt(args[2]) : 1;
        alpha = args.length > 3;

        load(args[0]);

        FileWriter fw = new FileWriter(new File(args[1]));
        foreachLine(line -> {
            line = line.substring(0, line.length() - 1);
            line += "\n";
            try {
                fw.write(line);
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        fw.close();
    }

    public void load(String path) throws IOException {
        img = ImageIO.read(new File(path));
    }

    public void foreachLine(Consumer<String> line) {
        line.accept(img.getWidth() + "," + img.getHeight() + ",");
        for (int y = mode; y < img.getHeight() - mode; y++) {
            for (int x = mode; x < img.getWidth() - mode; x++) {
                String out = "";

                for (int j = y - mode; j <= y + mode; j++) {
                    for (int i = x - mode; i <= x + mode; i++) {
                        // System.out.println("" + i + "," + j);
                        Color col = new Color(img.getRGB(i, j), true);

                        if (alpha) { // RGB or ARGB
                            out += (float) col.getAlpha() / 255f;
                            out += ",";
                        }
                        out += (float) col.getRed() / 255f;
                        out += ",";
                        out += (float) col.getGreen() / 255f;
                        out += ",";
                        out += (float) col.getBlue() / 255f;
                        out += ",";

                    }
                }
                // System.out.println("LINE");
                line.accept(out);
            }
        }
    }

    public static void main(String args[]) {
        try {
            new ImgToRaw(args);
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("DONE");
    }
}
