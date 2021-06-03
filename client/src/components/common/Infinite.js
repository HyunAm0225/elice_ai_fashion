import React, { useState, useEffect } from "react";
import InfiniteScroll from "react-infinite-scroll-component";
import { Loader } from "components/common/Loader";
import ItemInfo from "components/MainPage/ItemInfo";

export default function Infinite({ info }) {
  const [products, setProducts] = useState([]);
  const [count, setCount] = useState(0);

  // 추가 이미지 출력
  const fetchImages = (cnt) => {
    setProducts([...products, cnt, cnt + 1, cnt + 2, cnt + 3]);
    setCount(cnt + 4);
  };

  // 첫 접속시 이미지 출력
  useEffect(() => {
    fetchImages(count);
  }, []);

  return (
    <div style={{ width: "100%" }}>
      <InfiniteScroll
        style={{ display: "flex", flexWrap: "wrap" }}
        dataLength={products.length}
        next={() => fetchImages(count)}
        hasMore={count < 300 ? true : false}
        loader={<Loader />}
        endMessage={<p>You have seen it all</p>}
      >
        {products.map((idx) => (
          <ItemInfo key={idx} idx={idx} data={info[idx]} />
        ))}
      </InfiniteScroll>
    </div>
  );
}
