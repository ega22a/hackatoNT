<?php
    function createRandomString($lenght = 128) {
        $alphabet = str_split("qwertyuiopasdfghjklzxcvbnm1234567890");
        $return = "";
        for ($i = 0; $i < $lenght; $i++)
            $return .= $alphabet[random_int(0, count($alphabet) - 1)];
        return $return;
    }