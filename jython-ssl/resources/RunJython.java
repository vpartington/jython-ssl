import java.io.*;
import javax.script.*;

public class RunJython {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ScriptException {
      try {
        Reader scriptReader = new FileReader("https2ways.py");
        try {
          ScriptEngine engine = new ScriptEngineManager().getEngineByName("python");
          engine.eval(scriptReader);
        } finally {
          scriptReader.close();
        }
      } catch(Exception exc) {
        exc.printStackTrace();
      }
    }

}
