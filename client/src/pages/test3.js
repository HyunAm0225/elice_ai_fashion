// atom 을 읽기만 하는 컴포넌트
import { useRecoilValue } from "recoil";
import { countState } from "pages/test";

function ReadOnlyCount() {
  const count = useRecoilValue(countState); // 구독하는 atom 의 값만 반환

  return (
    <div>
      <h2>읽기 전용 컴포넌트</h2>
      <p>카운트 {count}</p>
    </div>
  );
}

export default ReadOnlyCount;
