import { useRecoilState } from "recoil";
import { testState } from "state/State";

export default function Test(msg) {
  const [test, setTest] = useRecoilState(testState);
  setTest(msg);
  alert(test);
}
