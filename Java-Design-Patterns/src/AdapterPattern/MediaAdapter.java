package AdapterPattern;

public class MediaAdapter implements MediaPlayer {

    AdvancedMediaPlayer advancedMediaPlayer;

    public MediaAdapter(String audioType) {
        if (audioType.equalsIgnoreCase("VLC")) advancedMediaPlayer = new VlcPlayer();
        else if (audioType.equalsIgnoreCase("MP4")) advancedMediaPlayer = new Mp4Player();
    }

    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("VLC")) advancedMediaPlayer.playVlc(fileName);
        else if (audioType.equalsIgnoreCase("MP4")) advancedMediaPlayer.playMp4(fileName);
    }
}
