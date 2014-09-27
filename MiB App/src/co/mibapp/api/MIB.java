package co.mibapp.api;

import android.graphics.Bitmap;

import java.util.ArrayList;

/**
 * Created by Gino on 9/27/2014.
 */
public interface MIB {

    public boolean login();

    public boolean createUsername(String username);

    public boolean addFriend(String username);

    public boolean removeFriend(String username);

    public boolean dropMessage(String msg);

    public boolean dropMesssage(String msg, double radius);

    public boolean dropMessage(Bitmap img);

    public boolean dropMessage(Bitmap img, double radius);

    public ArrayList<String> getFriendList();
}
