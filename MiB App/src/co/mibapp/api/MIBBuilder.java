package co.mibapp.api;

/**
 * Created by Gino on 9/27/2014.
 */
public class MIBBuilder {
    private static MIB _instance;


    public MIBBuilder() {
        //unused for now
    }

    public MIB getInstance() {
        if (_instance == null) {
            _instance = new MIBImplementation();
        }

        return _instance;
    }
}
