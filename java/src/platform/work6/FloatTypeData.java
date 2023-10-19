package platform.work6;

public class FloatTypeData extends SpecificTypeData<Float> {
    public FloatTypeData(Float data) {
        super(data);
    }

    @Override
    public void addData(Float data) {
        super.data += data;
    }
}
