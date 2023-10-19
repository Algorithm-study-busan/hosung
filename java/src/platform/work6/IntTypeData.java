package platform.work6;

public class IntTypeData extends SpecificTypeData<Integer> {
    public IntTypeData(Integer data) {
        super(data);
    }

    @Override
    public void addData(Integer data) {
        super.data += data;
    }
}
