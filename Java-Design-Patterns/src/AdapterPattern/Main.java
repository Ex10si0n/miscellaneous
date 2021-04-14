package AdapterPattern;

public class Main {
    public static void main(String[] args) {
        AudioPlayer audioPlayer = new AudioPlayer();

        audioPlayer.play("mp3", "Beyond the horizon.mp3");
        audioPlayer.play("mp4", "Alone.mp4");
        audioPlayer.play("vlc", "Far far away.vlc");
        audioPlayer.play("avi", "Mind me.avi");
    }
}
