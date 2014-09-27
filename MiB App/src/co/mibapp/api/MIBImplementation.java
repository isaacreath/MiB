package co.mibapp.api;

import android.graphics.Bitmap;

import java.util.ArrayList;

/**
 * Created by Gino on 9/27/2014.
 */

//package private
class MIBImplementation implements MIB {

    @Override
    public boolean login() {
        return false;
    }

    @Override
    public boolean createUsername(String username) {
        return false;
    }

    @Override
    public boolean addFriend(String username) {
        return false;
    }

    @Override
    public boolean removeFriend(String username) {
        return false;
    }

    @Override
    public boolean dropMessage(String msg) {
        return false;
    }

    @Override
    public boolean dropMesssage(String msg, double radius) {
        return false;
    }

    @Override
    public boolean dropMessage(Bitmap img) {
        return false;
    }

    @Override
    public boolean dropMessage(Bitmap img, double radius) {
        return false;
    }

    @Override
    public ArrayList<String> getFriendList() {
        return null;
    }
}
