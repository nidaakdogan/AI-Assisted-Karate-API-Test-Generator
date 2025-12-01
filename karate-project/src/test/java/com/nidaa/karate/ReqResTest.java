package com.nidaa.karate;

import com.intuit.karate.junit5.Karate;

public class ReqResTest {

    @Karate.Test
    Karate runReqResTests() {
        // Tüm .feature dosyalarını (manuel + AI üretimi) çalıştır
        return Karate.run("classpath:features")
                .relativeTo(getClass());
    }
}


