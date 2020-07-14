attribute \generator "nMigen"
attribute \top 1
attribute \nmigen.hierarchy "top"
module \top
  attribute \src "./reqwalker.py:29"
  wire width 1 input 0 \i_req
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/ir.py:526"
  wire width 1 input 1 \rst
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/ir.py:526"
  wire width 1 input 2 \clk
  attribute \src "./reqwalker.py:30"
  wire width 1 \o_busy
  attribute \src "./reqwalker.py:31"
  wire width 4 \state
  attribute \src "./reqwalker.py:31"
  wire width 4 \state$next
  attribute \src "./reqwalker.py:55"
  wire width 1 $1
  attribute \src "./reqwalker.py:55"
  cell $ne $2
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B 1'0
    connect \Y $1
  end
  process $group_0
    assign \o_busy 1'0
    assign \o_busy $1
    sync init
  end
  attribute \src "./reqwalker.py:57"
  wire width 4 \fsm_state
  attribute \src "./reqwalker.py:57"
  wire width 4 \fsm_state$next
  attribute \src "./reqwalker.py:28"
  wire width 32 \counter
  attribute \src "./reqwalker.py:28"
  wire width 32 \counter$next
  attribute \src "./reqwalker.py:69"
  wire width 1 $3
  attribute \src "./reqwalker.py:69"
  cell $eq $4
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $3
  end
  attribute \src "./reqwalker.py:77"
  wire width 1 $5
  attribute \src "./reqwalker.py:77"
  cell $eq $6
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $5
  end
  attribute \src "./reqwalker.py:85"
  wire width 1 $7
  attribute \src "./reqwalker.py:85"
  cell $eq $8
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $7
  end
  attribute \src "./reqwalker.py:93"
  wire width 1 $9
  attribute \src "./reqwalker.py:93"
  cell $eq $10
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $9
  end
  attribute \src "./reqwalker.py:101"
  wire width 1 $11
  attribute \src "./reqwalker.py:101"
  cell $eq $12
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $11
  end
  attribute \src "./reqwalker.py:109"
  wire width 1 $13
  attribute \src "./reqwalker.py:109"
  cell $eq $14
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $13
  end
  attribute \src "./reqwalker.py:117"
  wire width 1 $15
  attribute \src "./reqwalker.py:117"
  cell $eq $16
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $15
  end
  attribute \src "./reqwalker.py:125"
  wire width 1 $17
  attribute \src "./reqwalker.py:125"
  cell $eq $18
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $17
  end
  attribute \src "./reqwalker.py:133"
  wire width 1 $19
  attribute \src "./reqwalker.py:133"
  cell $eq $20
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $19
  end
  attribute \src "./reqwalker.py:141"
  wire width 1 $21
  attribute \src "./reqwalker.py:141"
  cell $eq $22
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $21
  end
  attribute \src "./reqwalker.py:149"
  wire width 1 $23
  attribute \src "./reqwalker.py:149"
  cell $eq $24
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $23
  end
  attribute \src "./reqwalker.py:157"
  wire width 1 $25
  attribute \src "./reqwalker.py:157"
  cell $eq $26
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $25
  end
  attribute \src "./reqwalker.py:165"
  wire width 1 $27
  attribute \src "./reqwalker.py:165"
  cell $eq $28
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $27
  end
  attribute \src "./reqwalker.py:173"
  wire width 1 $29
  attribute \src "./reqwalker.py:173"
  cell $eq $30
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $29
  end
  attribute \src "./reqwalker.py:181"
  wire width 1 $31
  attribute \src "./reqwalker.py:181"
  cell $eq $32
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $31
  end
  process $group_1
    assign \fsm_state$next \fsm_state
    attribute \src "./reqwalker.py:57"
    switch \fsm_state
      attribute \src "./reqwalker.py:58"
      attribute \nmigen.decoding "READY/0"
      case 4'0000
        assign \fsm_state$next 4'0000
        attribute \src "./reqwalker.py:62"
        switch { \i_req }
          attribute \src "./reqwalker.py:62"
          case 1'1
            assign \fsm_state$next 4'0001
        end
      attribute \src "./reqwalker.py:66"
      attribute \nmigen.decoding "WALK1/1"
      case 4'0001
        assign \fsm_state$next 4'0001
        attribute \src "./reqwalker.py:69"
        switch { $3 }
          attribute \src "./reqwalker.py:69"
          case 1'1
            assign \fsm_state$next 4'0010
        end
      attribute \src "./reqwalker.py:74"
      attribute \nmigen.decoding "WALK2/2"
      case 4'0010
        assign \fsm_state$next 4'0010
        attribute \src "./reqwalker.py:77"
        switch { $5 }
          attribute \src "./reqwalker.py:77"
          case 1'1
            assign \fsm_state$next 4'0011
        end
      attribute \src "./reqwalker.py:82"
      attribute \nmigen.decoding "WALK3/3"
      case 4'0011
        assign \fsm_state$next 4'0011
        attribute \src "./reqwalker.py:85"
        switch { $7 }
          attribute \src "./reqwalker.py:85"
          case 1'1
            assign \fsm_state$next 4'0100
        end
      attribute \src "./reqwalker.py:90"
      attribute \nmigen.decoding "WALK4/4"
      case 4'0100
        assign \fsm_state$next 4'0100
        attribute \src "./reqwalker.py:93"
        switch { $9 }
          attribute \src "./reqwalker.py:93"
          case 1'1
            assign \fsm_state$next 4'0101
        end
      attribute \src "./reqwalker.py:98"
      attribute \nmigen.decoding "WALK5/5"
      case 4'0101
        assign \fsm_state$next 4'0101
        attribute \src "./reqwalker.py:101"
        switch { $11 }
          attribute \src "./reqwalker.py:101"
          case 1'1
            assign \fsm_state$next 4'0110
        end
      attribute \src "./reqwalker.py:106"
      attribute \nmigen.decoding "WALK6/6"
      case 4'0110
        assign \fsm_state$next 4'0110
        attribute \src "./reqwalker.py:109"
        switch { $13 }
          attribute \src "./reqwalker.py:109"
          case 1'1
            assign \fsm_state$next 4'0111
        end
      attribute \src "./reqwalker.py:114"
      attribute \nmigen.decoding "WALK7/7"
      case 4'0111
        assign \fsm_state$next 4'0111
        attribute \src "./reqwalker.py:117"
        switch { $15 }
          attribute \src "./reqwalker.py:117"
          case 1'1
            assign \fsm_state$next 4'1000
        end
      attribute \src "./reqwalker.py:122"
      attribute \nmigen.decoding "WALK8/8"
      case 4'1000
        assign \fsm_state$next 4'1000
        attribute \src "./reqwalker.py:125"
        switch { $17 }
          attribute \src "./reqwalker.py:125"
          case 1'1
            assign \fsm_state$next 4'1001
        end
      attribute \src "./reqwalker.py:130"
      attribute \nmigen.decoding "WALK9/9"
      case 4'1001
        assign \fsm_state$next 4'1001
        attribute \src "./reqwalker.py:133"
        switch { $19 }
          attribute \src "./reqwalker.py:133"
          case 1'1
            assign \fsm_state$next 4'1010
        end
      attribute \src "./reqwalker.py:138"
      attribute \nmigen.decoding "WALK10/10"
      case 4'1010
        assign \fsm_state$next 4'1010
        attribute \src "./reqwalker.py:141"
        switch { $21 }
          attribute \src "./reqwalker.py:141"
          case 1'1
            assign \fsm_state$next 4'1011
        end
      attribute \src "./reqwalker.py:146"
      attribute \nmigen.decoding "WALK11/11"
      case 4'1011
        assign \fsm_state$next 4'1011
        attribute \src "./reqwalker.py:149"
        switch { $23 }
          attribute \src "./reqwalker.py:149"
          case 1'1
            assign \fsm_state$next 4'1100
        end
      attribute \src "./reqwalker.py:154"
      attribute \nmigen.decoding "WALK12/12"
      case 4'1100
        assign \fsm_state$next 4'1100
        attribute \src "./reqwalker.py:157"
        switch { $25 }
          attribute \src "./reqwalker.py:157"
          case 1'1
            assign \fsm_state$next 4'1101
        end
      attribute \src "./reqwalker.py:162"
      attribute \nmigen.decoding "WALK13/13"
      case 4'1101
        assign \fsm_state$next 4'1101
        attribute \src "./reqwalker.py:165"
        switch { $27 }
          attribute \src "./reqwalker.py:165"
          case 1'1
            assign \fsm_state$next 4'1110
        end
      attribute \src "./reqwalker.py:170"
      attribute \nmigen.decoding "WALK14/14"
      case 4'1110
        assign \fsm_state$next 4'1110
        attribute \src "./reqwalker.py:173"
        switch { $29 }
          attribute \src "./reqwalker.py:173"
          case 1'1
            assign \fsm_state$next 4'1111
        end
      attribute \src "./reqwalker.py:178"
      attribute \nmigen.decoding "WALK15/15"
      case 4'1111
        assign \fsm_state$next 4'1111
        attribute \src "./reqwalker.py:181"
        switch { $31 }
          attribute \src "./reqwalker.py:181"
          case 1'1
            assign \fsm_state$next 4'0000
        end
    end
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \fsm_state$next 4'0000
    end
    sync init
      update \fsm_state 4'0000
    sync posedge \clk
      update \fsm_state \fsm_state$next
  end
  attribute \src "./reqwalker.py:27"
  wire width 8 \leds
  attribute \src "./reqwalker.py:27"
  wire width 8 \leds$next
  attribute \src "./reqwalker.py:69"
  wire width 1 $33
  attribute \src "./reqwalker.py:69"
  cell $eq $34
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $33
  end
  attribute \src "./reqwalker.py:77"
  wire width 1 $35
  attribute \src "./reqwalker.py:77"
  cell $eq $36
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $35
  end
  attribute \src "./reqwalker.py:85"
  wire width 1 $37
  attribute \src "./reqwalker.py:85"
  cell $eq $38
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $37
  end
  attribute \src "./reqwalker.py:93"
  wire width 1 $39
  attribute \src "./reqwalker.py:93"
  cell $eq $40
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $39
  end
  attribute \src "./reqwalker.py:101"
  wire width 1 $41
  attribute \src "./reqwalker.py:101"
  cell $eq $42
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $41
  end
  attribute \src "./reqwalker.py:109"
  wire width 1 $43
  attribute \src "./reqwalker.py:109"
  cell $eq $44
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $43
  end
  attribute \src "./reqwalker.py:117"
  wire width 1 $45
  attribute \src "./reqwalker.py:117"
  cell $eq $46
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $45
  end
  attribute \src "./reqwalker.py:125"
  wire width 1 $47
  attribute \src "./reqwalker.py:125"
  cell $eq $48
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $47
  end
  attribute \src "./reqwalker.py:133"
  wire width 1 $49
  attribute \src "./reqwalker.py:133"
  cell $eq $50
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $49
  end
  attribute \src "./reqwalker.py:141"
  wire width 1 $51
  attribute \src "./reqwalker.py:141"
  cell $eq $52
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $51
  end
  attribute \src "./reqwalker.py:149"
  wire width 1 $53
  attribute \src "./reqwalker.py:149"
  cell $eq $54
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $53
  end
  attribute \src "./reqwalker.py:157"
  wire width 1 $55
  attribute \src "./reqwalker.py:157"
  cell $eq $56
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $55
  end
  attribute \src "./reqwalker.py:165"
  wire width 1 $57
  attribute \src "./reqwalker.py:165"
  cell $eq $58
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $57
  end
  attribute \src "./reqwalker.py:173"
  wire width 1 $59
  attribute \src "./reqwalker.py:173"
  cell $eq $60
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $59
  end
  attribute \src "./reqwalker.py:181"
  wire width 1 $61
  attribute \src "./reqwalker.py:181"
  cell $eq $62
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $61
  end
  process $group_2
    assign \leds$next \leds
    attribute \src "./reqwalker.py:57"
    switch \fsm_state
      attribute \src "./reqwalker.py:58"
      attribute \nmigen.decoding "READY/0"
      case 4'0000
        assign \leds$next 8'11111111
        attribute \src "./reqwalker.py:62"
        switch { \i_req }
          attribute \src "./reqwalker.py:62"
          case 1'1
            assign \leds$next 8'11111110
        end
      attribute \src "./reqwalker.py:66"
      attribute \nmigen.decoding "WALK1/1"
      case 4'0001
        attribute \src "./reqwalker.py:69"
        switch { $33 }
          attribute \src "./reqwalker.py:69"
          case 1'1
            assign \leds$next 8'11111101
        end
      attribute \src "./reqwalker.py:74"
      attribute \nmigen.decoding "WALK2/2"
      case 4'0010
        attribute \src "./reqwalker.py:77"
        switch { $35 }
          attribute \src "./reqwalker.py:77"
          case 1'1
            assign \leds$next 8'11111011
        end
      attribute \src "./reqwalker.py:82"
      attribute \nmigen.decoding "WALK3/3"
      case 4'0011
        attribute \src "./reqwalker.py:85"
        switch { $37 }
          attribute \src "./reqwalker.py:85"
          case 1'1
            assign \leds$next 8'11110111
        end
      attribute \src "./reqwalker.py:90"
      attribute \nmigen.decoding "WALK4/4"
      case 4'0100
        attribute \src "./reqwalker.py:93"
        switch { $39 }
          attribute \src "./reqwalker.py:93"
          case 1'1
            assign \leds$next 8'11101111
        end
      attribute \src "./reqwalker.py:98"
      attribute \nmigen.decoding "WALK5/5"
      case 4'0101
        attribute \src "./reqwalker.py:101"
        switch { $41 }
          attribute \src "./reqwalker.py:101"
          case 1'1
            assign \leds$next 8'11011111
        end
      attribute \src "./reqwalker.py:106"
      attribute \nmigen.decoding "WALK6/6"
      case 4'0110
        attribute \src "./reqwalker.py:109"
        switch { $43 }
          attribute \src "./reqwalker.py:109"
          case 1'1
            assign \leds$next 8'10111111
        end
      attribute \src "./reqwalker.py:114"
      attribute \nmigen.decoding "WALK7/7"
      case 4'0111
        attribute \src "./reqwalker.py:117"
        switch { $45 }
          attribute \src "./reqwalker.py:117"
          case 1'1
            assign \leds$next 8'01111111
        end
      attribute \src "./reqwalker.py:122"
      attribute \nmigen.decoding "WALK8/8"
      case 4'1000
        attribute \src "./reqwalker.py:125"
        switch { $47 }
          attribute \src "./reqwalker.py:125"
          case 1'1
            assign \leds$next 8'10111111
        end
      attribute \src "./reqwalker.py:130"
      attribute \nmigen.decoding "WALK9/9"
      case 4'1001
        attribute \src "./reqwalker.py:133"
        switch { $49 }
          attribute \src "./reqwalker.py:133"
          case 1'1
            assign \leds$next 8'11011111
        end
      attribute \src "./reqwalker.py:138"
      attribute \nmigen.decoding "WALK10/10"
      case 4'1010
        attribute \src "./reqwalker.py:141"
        switch { $51 }
          attribute \src "./reqwalker.py:141"
          case 1'1
            assign \leds$next 8'11101111
        end
      attribute \src "./reqwalker.py:146"
      attribute \nmigen.decoding "WALK11/11"
      case 4'1011
        attribute \src "./reqwalker.py:149"
        switch { $53 }
          attribute \src "./reqwalker.py:149"
          case 1'1
            assign \leds$next 8'11110111
        end
      attribute \src "./reqwalker.py:154"
      attribute \nmigen.decoding "WALK12/12"
      case 4'1100
        attribute \src "./reqwalker.py:157"
        switch { $55 }
          attribute \src "./reqwalker.py:157"
          case 1'1
            assign \leds$next 8'11111011
        end
      attribute \src "./reqwalker.py:162"
      attribute \nmigen.decoding "WALK13/13"
      case 4'1101
        attribute \src "./reqwalker.py:165"
        switch { $57 }
          attribute \src "./reqwalker.py:165"
          case 1'1
            assign \leds$next 8'11111101
        end
      attribute \src "./reqwalker.py:170"
      attribute \nmigen.decoding "WALK14/14"
      case 4'1110
        attribute \src "./reqwalker.py:173"
        switch { $59 }
          attribute \src "./reqwalker.py:173"
          case 1'1
            assign \leds$next 8'11111110
        end
      attribute \src "./reqwalker.py:178"
      attribute \nmigen.decoding "WALK15/15"
      case 4'1111
        attribute \src "./reqwalker.py:181"
        switch { $61 }
          attribute \src "./reqwalker.py:181"
          case 1'1
            assign \leds$next 8'11111111
        end
    end
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \leds$next 8'11111111
    end
    sync init
      update \leds 8'11111111
    sync posedge \clk
      update \leds \leds$next
  end
  attribute \src "./reqwalker.py:68"
  wire width 33 $63
  attribute \src "./reqwalker.py:68"
  wire width 33 $64
  attribute \src "./reqwalker.py:68"
  cell $add $65
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $64
  end
  connect $63 $64
  attribute \src "./reqwalker.py:69"
  wire width 1 $66
  attribute \src "./reqwalker.py:69"
  cell $eq $67
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $66
  end
  attribute \src "./reqwalker.py:76"
  wire width 33 $68
  attribute \src "./reqwalker.py:76"
  wire width 33 $69
  attribute \src "./reqwalker.py:76"
  cell $add $70
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $69
  end
  connect $68 $69
  attribute \src "./reqwalker.py:77"
  wire width 1 $71
  attribute \src "./reqwalker.py:77"
  cell $eq $72
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $71
  end
  attribute \src "./reqwalker.py:84"
  wire width 33 $73
  attribute \src "./reqwalker.py:84"
  wire width 33 $74
  attribute \src "./reqwalker.py:84"
  cell $add $75
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $74
  end
  connect $73 $74
  attribute \src "./reqwalker.py:85"
  wire width 1 $76
  attribute \src "./reqwalker.py:85"
  cell $eq $77
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $76
  end
  attribute \src "./reqwalker.py:92"
  wire width 33 $78
  attribute \src "./reqwalker.py:92"
  wire width 33 $79
  attribute \src "./reqwalker.py:92"
  cell $add $80
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $79
  end
  connect $78 $79
  attribute \src "./reqwalker.py:93"
  wire width 1 $81
  attribute \src "./reqwalker.py:93"
  cell $eq $82
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $81
  end
  attribute \src "./reqwalker.py:100"
  wire width 33 $83
  attribute \src "./reqwalker.py:100"
  wire width 33 $84
  attribute \src "./reqwalker.py:100"
  cell $add $85
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $84
  end
  connect $83 $84
  attribute \src "./reqwalker.py:101"
  wire width 1 $86
  attribute \src "./reqwalker.py:101"
  cell $eq $87
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $86
  end
  attribute \src "./reqwalker.py:108"
  wire width 33 $88
  attribute \src "./reqwalker.py:108"
  wire width 33 $89
  attribute \src "./reqwalker.py:108"
  cell $add $90
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $89
  end
  connect $88 $89
  attribute \src "./reqwalker.py:109"
  wire width 1 $91
  attribute \src "./reqwalker.py:109"
  cell $eq $92
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $91
  end
  attribute \src "./reqwalker.py:116"
  wire width 33 $93
  attribute \src "./reqwalker.py:116"
  wire width 33 $94
  attribute \src "./reqwalker.py:116"
  cell $add $95
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $94
  end
  connect $93 $94
  attribute \src "./reqwalker.py:117"
  wire width 1 $96
  attribute \src "./reqwalker.py:117"
  cell $eq $97
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $96
  end
  attribute \src "./reqwalker.py:124"
  wire width 33 $98
  attribute \src "./reqwalker.py:124"
  wire width 33 $99
  attribute \src "./reqwalker.py:124"
  cell $add $100
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $99
  end
  connect $98 $99
  attribute \src "./reqwalker.py:125"
  wire width 1 $101
  attribute \src "./reqwalker.py:125"
  cell $eq $102
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $101
  end
  attribute \src "./reqwalker.py:132"
  wire width 33 $103
  attribute \src "./reqwalker.py:132"
  wire width 33 $104
  attribute \src "./reqwalker.py:132"
  cell $add $105
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $104
  end
  connect $103 $104
  attribute \src "./reqwalker.py:133"
  wire width 1 $106
  attribute \src "./reqwalker.py:133"
  cell $eq $107
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $106
  end
  attribute \src "./reqwalker.py:140"
  wire width 33 $108
  attribute \src "./reqwalker.py:140"
  wire width 33 $109
  attribute \src "./reqwalker.py:140"
  cell $add $110
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $109
  end
  connect $108 $109
  attribute \src "./reqwalker.py:141"
  wire width 1 $111
  attribute \src "./reqwalker.py:141"
  cell $eq $112
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $111
  end
  attribute \src "./reqwalker.py:148"
  wire width 33 $113
  attribute \src "./reqwalker.py:148"
  wire width 33 $114
  attribute \src "./reqwalker.py:148"
  cell $add $115
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $114
  end
  connect $113 $114
  attribute \src "./reqwalker.py:149"
  wire width 1 $116
  attribute \src "./reqwalker.py:149"
  cell $eq $117
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $116
  end
  attribute \src "./reqwalker.py:156"
  wire width 33 $118
  attribute \src "./reqwalker.py:156"
  wire width 33 $119
  attribute \src "./reqwalker.py:156"
  cell $add $120
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $119
  end
  connect $118 $119
  attribute \src "./reqwalker.py:157"
  wire width 1 $121
  attribute \src "./reqwalker.py:157"
  cell $eq $122
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $121
  end
  attribute \src "./reqwalker.py:164"
  wire width 33 $123
  attribute \src "./reqwalker.py:164"
  wire width 33 $124
  attribute \src "./reqwalker.py:164"
  cell $add $125
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $124
  end
  connect $123 $124
  attribute \src "./reqwalker.py:165"
  wire width 1 $126
  attribute \src "./reqwalker.py:165"
  cell $eq $127
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $126
  end
  attribute \src "./reqwalker.py:172"
  wire width 33 $128
  attribute \src "./reqwalker.py:172"
  wire width 33 $129
  attribute \src "./reqwalker.py:172"
  cell $add $130
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $129
  end
  connect $128 $129
  attribute \src "./reqwalker.py:173"
  wire width 1 $131
  attribute \src "./reqwalker.py:173"
  cell $eq $132
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $131
  end
  attribute \src "./reqwalker.py:180"
  wire width 33 $133
  attribute \src "./reqwalker.py:180"
  wire width 33 $134
  attribute \src "./reqwalker.py:180"
  cell $add $135
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \counter
    connect \B 1'1
    connect \Y $134
  end
  connect $133 $134
  attribute \src "./reqwalker.py:181"
  wire width 1 $136
  attribute \src "./reqwalker.py:181"
  cell $eq $137
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $136
  end
  process $group_3
    assign \counter$next \counter
    attribute \src "./reqwalker.py:57"
    switch \fsm_state
      attribute \src "./reqwalker.py:58"
      attribute \nmigen.decoding "READY/0"
      case 4'0000
        assign \counter$next 32'00000000000000000000000000000000
      attribute \src "./reqwalker.py:66"
      attribute \nmigen.decoding "WALK1/1"
      case 4'0001
        assign \counter$next $63 [31:0]
        attribute \src "./reqwalker.py:69"
        switch { $66 }
          attribute \src "./reqwalker.py:69"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:74"
      attribute \nmigen.decoding "WALK2/2"
      case 4'0010
        assign \counter$next $68 [31:0]
        attribute \src "./reqwalker.py:77"
        switch { $71 }
          attribute \src "./reqwalker.py:77"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:82"
      attribute \nmigen.decoding "WALK3/3"
      case 4'0011
        assign \counter$next $73 [31:0]
        attribute \src "./reqwalker.py:85"
        switch { $76 }
          attribute \src "./reqwalker.py:85"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:90"
      attribute \nmigen.decoding "WALK4/4"
      case 4'0100
        assign \counter$next $78 [31:0]
        attribute \src "./reqwalker.py:93"
        switch { $81 }
          attribute \src "./reqwalker.py:93"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:98"
      attribute \nmigen.decoding "WALK5/5"
      case 4'0101
        assign \counter$next $83 [31:0]
        attribute \src "./reqwalker.py:101"
        switch { $86 }
          attribute \src "./reqwalker.py:101"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:106"
      attribute \nmigen.decoding "WALK6/6"
      case 4'0110
        assign \counter$next $88 [31:0]
        attribute \src "./reqwalker.py:109"
        switch { $91 }
          attribute \src "./reqwalker.py:109"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:114"
      attribute \nmigen.decoding "WALK7/7"
      case 4'0111
        assign \counter$next $93 [31:0]
        attribute \src "./reqwalker.py:117"
        switch { $96 }
          attribute \src "./reqwalker.py:117"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:122"
      attribute \nmigen.decoding "WALK8/8"
      case 4'1000
        assign \counter$next $98 [31:0]
        attribute \src "./reqwalker.py:125"
        switch { $101 }
          attribute \src "./reqwalker.py:125"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:130"
      attribute \nmigen.decoding "WALK9/9"
      case 4'1001
        assign \counter$next $103 [31:0]
        attribute \src "./reqwalker.py:133"
        switch { $106 }
          attribute \src "./reqwalker.py:133"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:138"
      attribute \nmigen.decoding "WALK10/10"
      case 4'1010
        assign \counter$next $108 [31:0]
        attribute \src "./reqwalker.py:141"
        switch { $111 }
          attribute \src "./reqwalker.py:141"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:146"
      attribute \nmigen.decoding "WALK11/11"
      case 4'1011
        assign \counter$next $113 [31:0]
        attribute \src "./reqwalker.py:149"
        switch { $116 }
          attribute \src "./reqwalker.py:149"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:154"
      attribute \nmigen.decoding "WALK12/12"
      case 4'1100
        assign \counter$next $118 [31:0]
        attribute \src "./reqwalker.py:157"
        switch { $121 }
          attribute \src "./reqwalker.py:157"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:162"
      attribute \nmigen.decoding "WALK13/13"
      case 4'1101
        assign \counter$next $123 [31:0]
        attribute \src "./reqwalker.py:165"
        switch { $126 }
          attribute \src "./reqwalker.py:165"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:170"
      attribute \nmigen.decoding "WALK14/14"
      case 4'1110
        assign \counter$next $128 [31:0]
        attribute \src "./reqwalker.py:173"
        switch { $131 }
          attribute \src "./reqwalker.py:173"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
      attribute \src "./reqwalker.py:178"
      attribute \nmigen.decoding "WALK15/15"
      case 4'1111
        assign \counter$next $133 [31:0]
        attribute \src "./reqwalker.py:181"
        switch { $136 }
          attribute \src "./reqwalker.py:181"
          case 1'1
            assign \counter$next 32'00000000000000000000000000000000
        end
    end
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \counter$next 32'00000000000000000000000000000000
    end
    sync init
      update \counter 32'00000000000000000000000000000000
    sync posedge \clk
      update \counter \counter$next
  end
  attribute \src "./reqwalker.py:69"
  wire width 1 $138
  attribute \src "./reqwalker.py:69"
  cell $eq $139
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $138
  end
  attribute \src "./reqwalker.py:77"
  wire width 1 $140
  attribute \src "./reqwalker.py:77"
  cell $eq $141
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $140
  end
  attribute \src "./reqwalker.py:85"
  wire width 1 $142
  attribute \src "./reqwalker.py:85"
  cell $eq $143
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $142
  end
  attribute \src "./reqwalker.py:93"
  wire width 1 $144
  attribute \src "./reqwalker.py:93"
  cell $eq $145
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $144
  end
  attribute \src "./reqwalker.py:101"
  wire width 1 $146
  attribute \src "./reqwalker.py:101"
  cell $eq $147
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $146
  end
  attribute \src "./reqwalker.py:109"
  wire width 1 $148
  attribute \src "./reqwalker.py:109"
  cell $eq $149
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $148
  end
  attribute \src "./reqwalker.py:117"
  wire width 1 $150
  attribute \src "./reqwalker.py:117"
  cell $eq $151
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $150
  end
  attribute \src "./reqwalker.py:125"
  wire width 1 $152
  attribute \src "./reqwalker.py:125"
  cell $eq $153
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $152
  end
  attribute \src "./reqwalker.py:133"
  wire width 1 $154
  attribute \src "./reqwalker.py:133"
  cell $eq $155
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $154
  end
  attribute \src "./reqwalker.py:141"
  wire width 1 $156
  attribute \src "./reqwalker.py:141"
  cell $eq $157
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $156
  end
  attribute \src "./reqwalker.py:149"
  wire width 1 $158
  attribute \src "./reqwalker.py:149"
  cell $eq $159
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $158
  end
  attribute \src "./reqwalker.py:157"
  wire width 1 $160
  attribute \src "./reqwalker.py:157"
  cell $eq $161
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $160
  end
  attribute \src "./reqwalker.py:165"
  wire width 1 $162
  attribute \src "./reqwalker.py:165"
  cell $eq $163
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $162
  end
  attribute \src "./reqwalker.py:173"
  wire width 1 $164
  attribute \src "./reqwalker.py:173"
  cell $eq $165
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $164
  end
  attribute \src "./reqwalker.py:181"
  wire width 1 $166
  attribute \src "./reqwalker.py:181"
  cell $eq $167
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 2'11
    connect \Y $166
  end
  process $group_4
    assign \state$next \state
    attribute \src "./reqwalker.py:57"
    switch \fsm_state
      attribute \src "./reqwalker.py:58"
      attribute \nmigen.decoding "READY/0"
      case 4'0000
        attribute \src "./reqwalker.py:62"
        switch { \i_req }
          attribute \src "./reqwalker.py:62"
          case 1'1
            assign \state$next 4'0001
        end
      attribute \src "./reqwalker.py:66"
      attribute \nmigen.decoding "WALK1/1"
      case 4'0001
        attribute \src "./reqwalker.py:69"
        switch { $138 }
          attribute \src "./reqwalker.py:69"
          case 1'1
            assign \state$next 4'0010
        end
      attribute \src "./reqwalker.py:74"
      attribute \nmigen.decoding "WALK2/2"
      case 4'0010
        attribute \src "./reqwalker.py:77"
        switch { $140 }
          attribute \src "./reqwalker.py:77"
          case 1'1
            assign \state$next 4'0011
        end
      attribute \src "./reqwalker.py:82"
      attribute \nmigen.decoding "WALK3/3"
      case 4'0011
        attribute \src "./reqwalker.py:85"
        switch { $142 }
          attribute \src "./reqwalker.py:85"
          case 1'1
            assign \state$next 4'0100
        end
      attribute \src "./reqwalker.py:90"
      attribute \nmigen.decoding "WALK4/4"
      case 4'0100
        attribute \src "./reqwalker.py:93"
        switch { $144 }
          attribute \src "./reqwalker.py:93"
          case 1'1
            assign \state$next 4'0101
        end
      attribute \src "./reqwalker.py:98"
      attribute \nmigen.decoding "WALK5/5"
      case 4'0101
        attribute \src "./reqwalker.py:101"
        switch { $146 }
          attribute \src "./reqwalker.py:101"
          case 1'1
            assign \state$next 4'0110
        end
      attribute \src "./reqwalker.py:106"
      attribute \nmigen.decoding "WALK6/6"
      case 4'0110
        attribute \src "./reqwalker.py:109"
        switch { $148 }
          attribute \src "./reqwalker.py:109"
          case 1'1
            assign \state$next 4'0111
        end
      attribute \src "./reqwalker.py:114"
      attribute \nmigen.decoding "WALK7/7"
      case 4'0111
        attribute \src "./reqwalker.py:117"
        switch { $150 }
          attribute \src "./reqwalker.py:117"
          case 1'1
            assign \state$next 4'1000
        end
      attribute \src "./reqwalker.py:122"
      attribute \nmigen.decoding "WALK8/8"
      case 4'1000
        attribute \src "./reqwalker.py:125"
        switch { $152 }
          attribute \src "./reqwalker.py:125"
          case 1'1
            assign \state$next 4'1001
        end
      attribute \src "./reqwalker.py:130"
      attribute \nmigen.decoding "WALK9/9"
      case 4'1001
        attribute \src "./reqwalker.py:133"
        switch { $154 }
          attribute \src "./reqwalker.py:133"
          case 1'1
            assign \state$next 4'1010
        end
      attribute \src "./reqwalker.py:138"
      attribute \nmigen.decoding "WALK10/10"
      case 4'1010
        attribute \src "./reqwalker.py:141"
        switch { $156 }
          attribute \src "./reqwalker.py:141"
          case 1'1
            assign \state$next 4'1011
        end
      attribute \src "./reqwalker.py:146"
      attribute \nmigen.decoding "WALK11/11"
      case 4'1011
        attribute \src "./reqwalker.py:149"
        switch { $158 }
          attribute \src "./reqwalker.py:149"
          case 1'1
            assign \state$next 4'1100
        end
      attribute \src "./reqwalker.py:154"
      attribute \nmigen.decoding "WALK12/12"
      case 4'1100
        attribute \src "./reqwalker.py:157"
        switch { $160 }
          attribute \src "./reqwalker.py:157"
          case 1'1
            assign \state$next 4'1101
        end
      attribute \src "./reqwalker.py:162"
      attribute \nmigen.decoding "WALK13/13"
      case 4'1101
        attribute \src "./reqwalker.py:165"
        switch { $162 }
          attribute \src "./reqwalker.py:165"
          case 1'1
            assign \state$next 4'1110
        end
      attribute \src "./reqwalker.py:170"
      attribute \nmigen.decoding "WALK14/14"
      case 4'1110
        attribute \src "./reqwalker.py:173"
        switch { $164 }
          attribute \src "./reqwalker.py:173"
          case 1'1
            assign \state$next 4'1111
        end
      attribute \src "./reqwalker.py:178"
      attribute \nmigen.decoding "WALK15/15"
      case 4'1111
        attribute \src "./reqwalker.py:181"
        switch { $166 }
          attribute \src "./reqwalker.py:181"
          case 1'1
            assign \state$next 4'0000
        end
    end
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \state$next 4'0000
    end
    sync init
      update \state 4'0000
    sync posedge \clk
      update \state \state$next
  end
  attribute \src "./reqwalker.py:191"
  wire width 1 \f_past_valid
  attribute \src "./reqwalker.py:191"
  wire width 1 \f_past_valid$next
  process $group_5
    assign \f_past_valid$next \f_past_valid
    assign \f_past_valid$next 1'1
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \f_past_valid$next 1'0
    end
    sync init
      update \f_past_valid 1'0
    sync posedge \clk
      update \f_past_valid \f_past_valid$next
  end
  attribute \src "./reqwalker.py:194"
  wire width 32 \f_pastn_counter
  attribute \src "./reqwalker.py:194"
  wire width 32 \f_pastn_counter$next
  attribute \src "./reqwalker.py:195"
  wire width 33 $168
  attribute \src "./reqwalker.py:195"
  wire width 33 $169
  attribute \src "./reqwalker.py:195"
  cell $add $170
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A \f_pastn_counter
    connect \B 1'1
    connect \Y $169
  end
  connect $168 $169
  attribute \src "./reqwalker.py:196"
  wire width 1 $171
  attribute \src "./reqwalker.py:196"
  cell $eq $172
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_counter
    connect \B 2'11
    connect \Y $171
  end
  process $group_6
    assign \f_pastn_counter$next \f_pastn_counter
    assign \f_pastn_counter$next $168 [31:0]
    attribute \src "./reqwalker.py:196"
    switch { $171 }
      attribute \src "./reqwalker.py:196"
      case 1'1
        assign \f_pastn_counter$next \f_pastn_counter
    end
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \f_pastn_counter$next 32'00000000000000000000000000000000
    end
    sync init
      update \f_pastn_counter 32'00000000000000000000000000000000
    sync posedge \clk
      update \f_pastn_counter \f_pastn_counter$next
  end
  attribute \src "./reqwalker.py:193"
  wire width 1 \f_pastn_valid
  attribute \src "./reqwalker.py:193"
  wire width 1 \f_pastn_valid$next
  attribute \src "./reqwalker.py:196"
  wire width 1 $173
  attribute \src "./reqwalker.py:196"
  cell $eq $174
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_counter
    connect \B 2'11
    connect \Y $173
  end
  process $group_7
    assign \f_pastn_valid$next \f_pastn_valid
    attribute \src "./reqwalker.py:196"
    switch { $173 }
      attribute \src "./reqwalker.py:196"
      case 1'1
        assign \f_pastn_valid$next 1'1
    end
    attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \f_pastn_valid$next 1'0
    end
    sync init
      update \f_pastn_valid 1'0
    sync posedge \clk
      update \f_pastn_valid \f_pastn_valid$next
  end
  attribute \src "./reqwalker.py:206"
  wire width 1 $assert$en
  attribute \src "./reqwalker.py:206"
  wire width 1 $assert$check
  attribute \src "./reqwalker.py:206"
  wire width 1 $175
  attribute \src "./reqwalker.py:206"
  cell $eq $176
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111111
    connect \Y $175
  end
  attribute \src "./reqwalker.py:206"
  cell $assert $177
    connect \A $assert$check
    connect \EN $assert$en
  end
  process $group_8
    assign $assert$en 1'0
    assign $assert$check 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
        assign $assert$check $175
        assign $assert$en 1'1
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:208"
  wire width 1 $assert$en$178
  attribute \src "./reqwalker.py:208"
  wire width 1 $assert$check$179
  attribute \src "./reqwalker.py:208"
  wire width 1 $180
  attribute \src "./reqwalker.py:208"
  cell $eq $181
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111110
    connect \Y $180
  end
  attribute \src "./reqwalker.py:208"
  cell $assert $182
    connect \A $assert$check$179
    connect \EN $assert$en$178
  end
  process $group_10
    assign $assert$en$178 1'0
    assign $assert$check$179 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
        assign $assert$check$179 $180
        assign $assert$en$178 1'1
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:210"
  wire width 1 $assert$en$183
  attribute \src "./reqwalker.py:210"
  wire width 1 $assert$check$184
  attribute \src "./reqwalker.py:210"
  wire width 1 $185
  attribute \src "./reqwalker.py:210"
  cell $eq $186
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111101
    connect \Y $185
  end
  attribute \src "./reqwalker.py:210"
  cell $assert $187
    connect \A $assert$check$184
    connect \EN $assert$en$183
  end
  process $group_12
    assign $assert$en$183 1'0
    assign $assert$check$184 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
        assign $assert$check$184 $185
        assign $assert$en$183 1'1
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:212"
  wire width 1 $assert$en$188
  attribute \src "./reqwalker.py:212"
  wire width 1 $assert$check$189
  attribute \src "./reqwalker.py:212"
  wire width 1 $190
  attribute \src "./reqwalker.py:212"
  cell $eq $191
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111011
    connect \Y $190
  end
  attribute \src "./reqwalker.py:212"
  cell $assert $192
    connect \A $assert$check$189
    connect \EN $assert$en$188
  end
  process $group_14
    assign $assert$en$188 1'0
    assign $assert$check$189 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
        assign $assert$check$189 $190
        assign $assert$en$188 1'1
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:214"
  wire width 1 $assert$en$193
  attribute \src "./reqwalker.py:214"
  wire width 1 $assert$check$194
  attribute \src "./reqwalker.py:214"
  wire width 1 $195
  attribute \src "./reqwalker.py:214"
  cell $eq $196
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11110111
    connect \Y $195
  end
  attribute \src "./reqwalker.py:214"
  cell $assert $197
    connect \A $assert$check$194
    connect \EN $assert$en$193
  end
  process $group_16
    assign $assert$en$193 1'0
    assign $assert$check$194 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
        assign $assert$check$194 $195
        assign $assert$en$193 1'1
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:216"
  wire width 1 $assert$en$198
  attribute \src "./reqwalker.py:216"
  wire width 1 $assert$check$199
  attribute \src "./reqwalker.py:216"
  wire width 1 $200
  attribute \src "./reqwalker.py:216"
  cell $eq $201
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11101111
    connect \Y $200
  end
  attribute \src "./reqwalker.py:216"
  cell $assert $202
    connect \A $assert$check$199
    connect \EN $assert$en$198
  end
  process $group_18
    assign $assert$en$198 1'0
    assign $assert$check$199 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
        assign $assert$check$199 $200
        assign $assert$en$198 1'1
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:218"
  wire width 1 $assert$en$203
  attribute \src "./reqwalker.py:218"
  wire width 1 $assert$check$204
  attribute \src "./reqwalker.py:218"
  wire width 1 $205
  attribute \src "./reqwalker.py:218"
  cell $eq $206
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11011111
    connect \Y $205
  end
  attribute \src "./reqwalker.py:218"
  cell $assert $207
    connect \A $assert$check$204
    connect \EN $assert$en$203
  end
  process $group_20
    assign $assert$en$203 1'0
    assign $assert$check$204 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
        assign $assert$check$204 $205
        assign $assert$en$203 1'1
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:220"
  wire width 1 $assert$en$208
  attribute \src "./reqwalker.py:220"
  wire width 1 $assert$check$209
  attribute \src "./reqwalker.py:220"
  wire width 1 $210
  attribute \src "./reqwalker.py:220"
  cell $eq $211
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'10111111
    connect \Y $210
  end
  attribute \src "./reqwalker.py:220"
  cell $assert $212
    connect \A $assert$check$209
    connect \EN $assert$en$208
  end
  process $group_22
    assign $assert$en$208 1'0
    assign $assert$check$209 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
        assign $assert$check$209 $210
        assign $assert$en$208 1'1
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:222"
  wire width 1 $assert$en$213
  attribute \src "./reqwalker.py:222"
  wire width 1 $assert$check$214
  attribute \src "./reqwalker.py:222"
  wire width 1 $215
  attribute \src "./reqwalker.py:222"
  cell $eq $216
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'111
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 7'1111111
    connect \Y $215
  end
  attribute \src "./reqwalker.py:222"
  cell $assert $217
    connect \A $assert$check$214
    connect \EN $assert$en$213
  end
  process $group_24
    assign $assert$en$213 1'0
    assign $assert$check$214 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
        assign $assert$check$214 $215
        assign $assert$en$213 1'1
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:224"
  wire width 1 $assert$en$218
  attribute \src "./reqwalker.py:224"
  wire width 1 $assert$check$219
  attribute \src "./reqwalker.py:224"
  wire width 1 $220
  attribute \src "./reqwalker.py:224"
  cell $eq $221
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'10111111
    connect \Y $220
  end
  attribute \src "./reqwalker.py:224"
  cell $assert $222
    connect \A $assert$check$219
    connect \EN $assert$en$218
  end
  process $group_26
    assign $assert$en$218 1'0
    assign $assert$check$219 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
        assign $assert$check$219 $220
        assign $assert$en$218 1'1
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:226"
  wire width 1 $assert$en$223
  attribute \src "./reqwalker.py:226"
  wire width 1 $assert$check$224
  attribute \src "./reqwalker.py:226"
  wire width 1 $225
  attribute \src "./reqwalker.py:226"
  cell $eq $226
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11011111
    connect \Y $225
  end
  attribute \src "./reqwalker.py:226"
  cell $assert $227
    connect \A $assert$check$224
    connect \EN $assert$en$223
  end
  process $group_28
    assign $assert$en$223 1'0
    assign $assert$check$224 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
        assign $assert$check$224 $225
        assign $assert$en$223 1'1
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:228"
  wire width 1 $assert$en$228
  attribute \src "./reqwalker.py:228"
  wire width 1 $assert$check$229
  attribute \src "./reqwalker.py:228"
  wire width 1 $230
  attribute \src "./reqwalker.py:228"
  cell $eq $231
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11101111
    connect \Y $230
  end
  attribute \src "./reqwalker.py:228"
  cell $assert $232
    connect \A $assert$check$229
    connect \EN $assert$en$228
  end
  process $group_30
    assign $assert$en$228 1'0
    assign $assert$check$229 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
        assign $assert$check$229 $230
        assign $assert$en$228 1'1
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:230"
  wire width 1 $assert$en$233
  attribute \src "./reqwalker.py:230"
  wire width 1 $assert$check$234
  attribute \src "./reqwalker.py:230"
  wire width 1 $235
  attribute \src "./reqwalker.py:230"
  cell $eq $236
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11110111
    connect \Y $235
  end
  attribute \src "./reqwalker.py:230"
  cell $assert $237
    connect \A $assert$check$234
    connect \EN $assert$en$233
  end
  process $group_32
    assign $assert$en$233 1'0
    assign $assert$check$234 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
        assign $assert$check$234 $235
        assign $assert$en$233 1'1
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:232"
  wire width 1 $assert$en$238
  attribute \src "./reqwalker.py:232"
  wire width 1 $assert$check$239
  attribute \src "./reqwalker.py:232"
  wire width 1 $240
  attribute \src "./reqwalker.py:232"
  cell $eq $241
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111011
    connect \Y $240
  end
  attribute \src "./reqwalker.py:232"
  cell $assert $242
    connect \A $assert$check$239
    connect \EN $assert$en$238
  end
  process $group_34
    assign $assert$en$238 1'0
    assign $assert$check$239 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
        assign $assert$check$239 $240
        assign $assert$en$238 1'1
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:234"
  wire width 1 $assert$en$243
  attribute \src "./reqwalker.py:234"
  wire width 1 $assert$check$244
  attribute \src "./reqwalker.py:234"
  wire width 1 $245
  attribute \src "./reqwalker.py:234"
  cell $eq $246
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111101
    connect \Y $245
  end
  attribute \src "./reqwalker.py:234"
  cell $assert $247
    connect \A $assert$check$244
    connect \EN $assert$en$243
  end
  process $group_36
    assign $assert$en$243 1'0
    assign $assert$check$244 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
        assign $assert$check$244 $245
        assign $assert$en$243 1'1
      attribute \src "./reqwalker.py:235"
      case 4'1111
    end
    sync init
  end
  attribute \src "./reqwalker.py:236"
  wire width 1 $assert$en$248
  attribute \src "./reqwalker.py:236"
  wire width 1 $assert$check$249
  attribute \src "./reqwalker.py:236"
  wire width 1 $250
  attribute \src "./reqwalker.py:236"
  cell $eq $251
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 4'1000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 4'1000
    parameter \Y_WIDTH 1'1
    connect \A \leds
    connect \B 8'11111110
    connect \Y $250
  end
  attribute \src "./reqwalker.py:236"
  cell $assert $252
    connect \A $assert$check$249
    connect \EN $assert$en$248
  end
  process $group_38
    assign $assert$en$248 1'0
    assign $assert$check$249 1'0
    attribute \src "./reqwalker.py:204"
    switch \state
      attribute \src "./reqwalker.py:205"
      case 4'0000
      attribute \src "./reqwalker.py:207"
      case 4'0001
      attribute \src "./reqwalker.py:209"
      case 4'0010
      attribute \src "./reqwalker.py:211"
      case 4'0011
      attribute \src "./reqwalker.py:213"
      case 4'0100
      attribute \src "./reqwalker.py:215"
      case 4'0101
      attribute \src "./reqwalker.py:217"
      case 4'0110
      attribute \src "./reqwalker.py:219"
      case 4'0111
      attribute \src "./reqwalker.py:221"
      case 4'1000
      attribute \src "./reqwalker.py:223"
      case 4'1001
      attribute \src "./reqwalker.py:225"
      case 4'1010
      attribute \src "./reqwalker.py:227"
      case 4'1011
      attribute \src "./reqwalker.py:229"
      case 4'1100
      attribute \src "./reqwalker.py:231"
      case 4'1101
      attribute \src "./reqwalker.py:233"
      case 4'1110
      attribute \src "./reqwalker.py:235"
      case 4'1111
        assign $assert$check$249 $250
        assign $assert$en$248 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:242"
  wire width 1 $assert$en$253
  attribute \src "./reqwalker.py:242"
  wire width 1 $assert$check$254
  attribute \src "./reqwalker.py:242"
  wire width 1 $255
  attribute \src "./reqwalker.py:242"
  cell $lt $256
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'11
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 3'100
    connect \Y $255
  end
  attribute \src "./reqwalker.py:242"
  cell $assert $257
    connect \A $assert$check$254
    connect \EN $assert$en$253
  end
  process $group_40
    assign $assert$en$253 1'0
    assign $assert$check$254 1'0
    assign $assert$check$254 $255
    assign $assert$en$253 1'1
    sync init
  end
  attribute \src "./reqwalker.py:246"
  wire width 1 $assert$en$258
  attribute \src "./reqwalker.py:246"
  wire width 1 $assert$check$259
  attribute \src "./reqwalker.py:245"
  wire width 1 $260
  attribute \src "./reqwalker.py:245"
  cell $eq $261
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B 1'0
    connect \Y $260
  end
  attribute \src "./reqwalker.py:246"
  wire width 1 $262
  attribute \src "./reqwalker.py:246"
  cell $eq $263
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 1'0
    connect \Y $262
  end
  attribute \src "./reqwalker.py:246"
  cell $assert $264
    connect \A $assert$check$259
    connect \EN $assert$en$258
  end
  process $group_42
    assign $assert$en$258 1'0
    assign $assert$check$259 1'0
    attribute \src "./reqwalker.py:245"
    switch { $260 }
      attribute \src "./reqwalker.py:245"
      case 1'1
        assign $assert$check$259 $262
        assign $assert$en$258 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:250"
  wire width 1 $assert$en$265
  attribute \src "./reqwalker.py:250"
  wire width 1 $assert$check$266
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:277"
  wire width 4 $sample$s$state$sync$1
  attribute \src "./reqwalker.py:277"
  wire width 4 $sample$s$state$sync$1$next
  attribute \src "./reqwalker.py:249"
  wire width 1 $267
  attribute \src "./reqwalker.py:249"
  cell $eq $268
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B 1'0
    connect \Y $267
  end
  attribute \src "./reqwalker.py:249"
  wire width 1 $269
  attribute \src "./reqwalker.py:249"
  cell $and $270
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_past_valid
    connect \B $267
    connect \Y $269
  end
  attribute \src "./reqwalker.py:249"
  wire width 1 $271
  attribute \src "./reqwalker.py:249"
  cell $eq $272
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B 1'1
    connect \Y $271
  end
  attribute \src "./reqwalker.py:249"
  wire width 1 $273
  attribute \src "./reqwalker.py:249"
  cell $and $274
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $269
    connect \B $271
    connect \Y $273
  end
  attribute \src "./reqwalker.py:250"
  wire width 1 $275
  attribute \src "./reqwalker.py:250"
  cell $eq $276
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B 1'0
    connect \Y $275
  end
  attribute \src "./reqwalker.py:250"
  cell $assert $277
    connect \A $assert$check$266
    connect \EN $assert$en$265
  end
  process $group_44
    assign $assert$en$265 1'0
    assign $assert$check$266 1'0
    attribute \src "./reqwalker.py:249"
    switch { $273 }
      attribute \src "./reqwalker.py:249"
      case 1'1
        assign $assert$check$266 $275
        assign $assert$en$265 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:254"
  wire width 1 $assert$en$278
  attribute \src "./reqwalker.py:254"
  wire width 1 $assert$check$279
  attribute \src "./reqwalker.py:253"
  wire width 1 $280
  attribute \src "./reqwalker.py:253"
  cell $ne $281
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B 1'0
    connect \Y $280
  end
  attribute \src "./reqwalker.py:253"
  wire width 1 $282
  attribute \src "./reqwalker.py:253"
  cell $and $283
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_past_valid
    connect \B $280
    connect \Y $282
  end
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$1
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$1$next
  attribute \src "./reqwalker.py:254"
  wire width 33 $284
  attribute \src "./reqwalker.py:254"
  cell $add $285
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A $sample$s$counter$sync$1
    connect \B 1'1
    connect \Y $284
  end
  attribute \src "./reqwalker.py:254"
  wire width 33 $286
  attribute \src "./reqwalker.py:254"
  cell $mod $287
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100001
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'11
    parameter \Y_WIDTH 6'100001
    connect \A $284
    connect \B 3'100
    connect \Y $286
  end
  attribute \src "./reqwalker.py:254"
  wire width 33 $288
  attribute \src "./reqwalker.py:254"
  wire width 33 $289
  attribute \src "./reqwalker.py:254"
  cell $add $290
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 6'100001
    connect \A $sample$s$counter$sync$1
    connect \B 1'1
    connect \Y $289
  end
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  wire width 1 $291
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  cell $eq $292
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100001
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $289
    connect \B 1'0
    connect \Y $291
  end
  attribute \src "./reqwalker.py:254"
  cell $mux $293
    parameter \WIDTH 6'100001
    connect \A $286
    connect \B 33'000000000000000000000000000000000
    connect \S $291
    connect \Y $288
  end
  attribute \src "./reqwalker.py:254"
  wire width 1 $294
  attribute \src "./reqwalker.py:254"
  cell $eq $295
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 6'100001
    parameter \Y_WIDTH 1'1
    connect \A \counter
    connect \B $288
    connect \Y $294
  end
  attribute \src "./reqwalker.py:254"
  cell $assert $296
    connect \A $assert$check$279
    connect \EN $assert$en$278
  end
  process $group_46
    assign $assert$en$278 1'0
    assign $assert$check$279 1'0
    attribute \src "./reqwalker.py:253"
    switch { $282 }
      attribute \src "./reqwalker.py:253"
      case 1'1
        assign $assert$check$279 $294
        assign $assert$en$278 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:260"
  wire width 1 $assert$en$297
  attribute \src "./reqwalker.py:260"
  wire width 1 $assert$check$298
  attribute \src "./reqwalker.py:260"
  wire width 1 $299
  attribute \src "./reqwalker.py:260"
  cell $ne $300
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B 1'0
    connect \Y $299
  end
  attribute \src "./reqwalker.py:260"
  wire width 1 $301
  attribute \src "./reqwalker.py:260"
  cell $eq $302
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \o_busy
    connect \B $299
    connect \Y $301
  end
  attribute \src "./reqwalker.py:260"
  cell $assert $303
    connect \A $assert$check$298
    connect \EN $assert$en$297
  end
  process $group_48
    assign $assert$en$297 1'0
    assign $assert$check$298 1'0
    assign $assert$check$298 $301
    assign $assert$en$297 1'1
    sync init
  end
  attribute \src "./reqwalker.py:266"
  wire width 1 $assert$en$304
  attribute \src "./reqwalker.py:266"
  wire width 1 $assert$check$305
  attribute \src "./reqwalker.py:266"
  wire width 1 $306
  attribute \src "./reqwalker.py:266"
  cell $lt $307
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B 5'10000
    connect \Y $306
  end
  attribute \src "./reqwalker.py:266"
  cell $assert $308
    connect \A $assert$check$305
    connect \EN $assert$en$304
  end
  process $group_50
    assign $assert$en$304 1'0
    assign $assert$check$305 1'0
    assign $assert$check$305 $306
    assign $assert$en$304 1'1
    sync init
  end
  attribute \src "./reqwalker.py:270"
  wire width 1 $assert$en$309
  attribute \src "./reqwalker.py:270"
  wire width 1 $assert$check$310
  attribute \src "./reqwalker.py:269"
  wire width 1 $311
  attribute \src "./reqwalker.py:269"
  cell $eq $312
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B 1'0
    connect \Y $311
  end
  attribute \src "./reqwalker.py:269"
  wire width 1 $313
  attribute \src "./reqwalker.py:269"
  cell $and $314
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_past_valid
    connect \B $311
    connect \Y $313
  end
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:269"
  wire width 1 $sample$s$i_req$sync$1
  attribute \src "./reqwalker.py:269"
  wire width 1 $sample$s$i_req$sync$1$next
  attribute \src "./reqwalker.py:269"
  wire width 1 $315
  attribute \src "./reqwalker.py:269"
  cell $and $316
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $313
    connect \B $sample$s$i_req$sync$1
    connect \Y $315
  end
  attribute \src "./reqwalker.py:270"
  wire width 1 $317
  attribute \src "./reqwalker.py:270"
  cell $eq $318
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B 1'1
    connect \Y $317
  end
  attribute \src "./reqwalker.py:270"
  cell $assert $319
    connect \A $assert$check$310
    connect \EN $assert$en$309
  end
  process $group_52
    assign $assert$en$309 1'0
    assign $assert$check$310 1'0
    attribute \src "./reqwalker.py:269"
    switch { $315 }
      attribute \src "./reqwalker.py:269"
      case 1'1
        assign $assert$check$310 $317
        assign $assert$en$309 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$en$320
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$check$321
  attribute \src "./reqwalker.py:275"
  wire width 1 $322
  attribute \src "./reqwalker.py:275"
  cell $ne $323
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B 1'0
    connect \Y $322
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $324
  attribute \src "./reqwalker.py:275"
  cell $and $325
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $322
    connect \Y $324
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $326
  attribute \src "./reqwalker.py:276"
  cell $eq $327
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$1
    connect \B 2'11
    connect \Y $326
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $328
  attribute \src "./reqwalker.py:276"
  cell $and $329
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $324
    connect \B $326
    connect \Y $328
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $330
  attribute \src "./reqwalker.py:277"
  cell $eq $331
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'100
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B $sample$s$state$sync$1
    connect \Y $330
  end
  attribute \src "./reqwalker.py:277"
  cell $assert $332
    connect \A $assert$check$321
    connect \EN $assert$en$320
  end
  process $group_54
    assign $assert$en$320 1'0
    assign $assert$check$321 1'0
    attribute \src "./reqwalker.py:276"
    switch { $328 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$321 $330
        assign $assert$en$320 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$en$333
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$check$334
  attribute \src "./reqwalker.py:275"
  wire width 1 $335
  attribute \src "./reqwalker.py:275"
  cell $ne $336
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B 1'0
    connect \Y $335
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $337
  attribute \src "./reqwalker.py:275"
  cell $and $338
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $335
    connect \Y $337
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $339
  attribute \src "./reqwalker.py:276"
  cell $eq $340
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$1
    connect \B 2'11
    connect \Y $339
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $341
  attribute \src "./reqwalker.py:276"
  cell $and $342
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $337
    connect \B $339
    connect \Y $341
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $343
  attribute \src "./reqwalker.py:278"
  cell $add $344
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$1
    connect \B 1'1
    connect \Y $343
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $345
  attribute \src "./reqwalker.py:278"
  cell $mod $346
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 3'101
    connect \A $343
    connect \B 5'10000
    connect \Y $345
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $347
  attribute \src "./reqwalker.py:278"
  wire width 5 $348
  attribute \src "./reqwalker.py:278"
  cell $add $349
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$1
    connect \B 1'1
    connect \Y $348
  end
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  wire width 1 $350
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  cell $eq $351
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $348
    connect \B 1'0
    connect \Y $350
  end
  attribute \src "./reqwalker.py:278"
  cell $mux $352
    parameter \WIDTH 3'101
    connect \A $345
    connect \B 5'00000
    connect \S $350
    connect \Y $347
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $353
  attribute \src "./reqwalker.py:278"
  cell $eq $354
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B $347
    connect \Y $353
  end
  attribute \src "./reqwalker.py:278"
  cell $assert $355
    connect \A $assert$check$334
    connect \EN $assert$en$333
  end
  process $group_56
    assign $assert$en$333 1'0
    assign $assert$check$334 1'0
    attribute \src "./reqwalker.py:276"
    switch { $341 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$334 $353
        assign $assert$en$333 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$en$356
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$check$357
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:275"
  wire width 4 $sample$s$state$sync$2
  attribute \src "./reqwalker.py:275"
  wire width 4 $sample$s$state$sync$2$next
  attribute \src "./reqwalker.py:275"
  wire width 1 $358
  attribute \src "./reqwalker.py:275"
  cell $ne $359
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$2
    connect \B 1'0
    connect \Y $358
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $360
  attribute \src "./reqwalker.py:275"
  cell $and $361
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $358
    connect \Y $360
  end
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$2
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$2$next
  attribute \src "./reqwalker.py:276"
  wire width 1 $362
  attribute \src "./reqwalker.py:276"
  cell $eq $363
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$2
    connect \B 2'10
    connect \Y $362
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $364
  attribute \src "./reqwalker.py:276"
  cell $and $365
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $360
    connect \B $362
    connect \Y $364
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $366
  attribute \src "./reqwalker.py:277"
  cell $eq $367
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'100
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B $sample$s$state$sync$2
    connect \Y $366
  end
  attribute \src "./reqwalker.py:277"
  cell $assert $368
    connect \A $assert$check$357
    connect \EN $assert$en$356
  end
  process $group_58
    assign $assert$en$356 1'0
    assign $assert$check$357 1'0
    attribute \src "./reqwalker.py:276"
    switch { $364 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$357 $366
        assign $assert$en$356 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$en$369
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$check$370
  attribute \src "./reqwalker.py:275"
  wire width 1 $371
  attribute \src "./reqwalker.py:275"
  cell $ne $372
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$2
    connect \B 1'0
    connect \Y $371
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $373
  attribute \src "./reqwalker.py:275"
  cell $and $374
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $371
    connect \Y $373
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $375
  attribute \src "./reqwalker.py:276"
  cell $eq $376
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 2'10
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$2
    connect \B 2'10
    connect \Y $375
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $377
  attribute \src "./reqwalker.py:276"
  cell $and $378
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $373
    connect \B $375
    connect \Y $377
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $379
  attribute \src "./reqwalker.py:278"
  cell $add $380
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$2
    connect \B 1'1
    connect \Y $379
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $381
  attribute \src "./reqwalker.py:278"
  cell $mod $382
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 3'101
    connect \A $379
    connect \B 5'10000
    connect \Y $381
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $383
  attribute \src "./reqwalker.py:278"
  wire width 5 $384
  attribute \src "./reqwalker.py:278"
  cell $add $385
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$2
    connect \B 1'1
    connect \Y $384
  end
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  wire width 1 $386
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  cell $eq $387
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $384
    connect \B 1'0
    connect \Y $386
  end
  attribute \src "./reqwalker.py:278"
  cell $mux $388
    parameter \WIDTH 3'101
    connect \A $381
    connect \B 5'00000
    connect \S $386
    connect \Y $383
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $389
  attribute \src "./reqwalker.py:278"
  cell $eq $390
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B $383
    connect \Y $389
  end
  attribute \src "./reqwalker.py:278"
  cell $assert $391
    connect \A $assert$check$370
    connect \EN $assert$en$369
  end
  process $group_60
    assign $assert$en$369 1'0
    assign $assert$check$370 1'0
    attribute \src "./reqwalker.py:276"
    switch { $377 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$370 $389
        assign $assert$en$369 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$en$392
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$check$393
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:275"
  wire width 4 $sample$s$state$sync$3
  attribute \src "./reqwalker.py:275"
  wire width 4 $sample$s$state$sync$3$next
  attribute \src "./reqwalker.py:275"
  wire width 1 $394
  attribute \src "./reqwalker.py:275"
  cell $ne $395
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$3
    connect \B 1'0
    connect \Y $394
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $396
  attribute \src "./reqwalker.py:275"
  cell $and $397
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $394
    connect \Y $396
  end
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$3
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$3$next
  attribute \src "./reqwalker.py:276"
  wire width 1 $398
  attribute \src "./reqwalker.py:276"
  cell $eq $399
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$3
    connect \B 1'1
    connect \Y $398
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $400
  attribute \src "./reqwalker.py:276"
  cell $and $401
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $396
    connect \B $398
    connect \Y $400
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $402
  attribute \src "./reqwalker.py:277"
  cell $eq $403
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'100
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B $sample$s$state$sync$3
    connect \Y $402
  end
  attribute \src "./reqwalker.py:277"
  cell $assert $404
    connect \A $assert$check$393
    connect \EN $assert$en$392
  end
  process $group_62
    assign $assert$en$392 1'0
    assign $assert$check$393 1'0
    attribute \src "./reqwalker.py:276"
    switch { $400 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$393 $402
        assign $assert$en$392 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$en$405
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$check$406
  attribute \src "./reqwalker.py:275"
  wire width 1 $407
  attribute \src "./reqwalker.py:275"
  cell $ne $408
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$3
    connect \B 1'0
    connect \Y $407
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $409
  attribute \src "./reqwalker.py:275"
  cell $and $410
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $407
    connect \Y $409
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $411
  attribute \src "./reqwalker.py:276"
  cell $eq $412
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$3
    connect \B 1'1
    connect \Y $411
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $413
  attribute \src "./reqwalker.py:276"
  cell $and $414
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $409
    connect \B $411
    connect \Y $413
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $415
  attribute \src "./reqwalker.py:278"
  cell $add $416
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$3
    connect \B 1'1
    connect \Y $415
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $417
  attribute \src "./reqwalker.py:278"
  cell $mod $418
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 3'101
    connect \A $415
    connect \B 5'10000
    connect \Y $417
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $419
  attribute \src "./reqwalker.py:278"
  wire width 5 $420
  attribute \src "./reqwalker.py:278"
  cell $add $421
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$3
    connect \B 1'1
    connect \Y $420
  end
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  wire width 1 $422
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  cell $eq $423
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $420
    connect \B 1'0
    connect \Y $422
  end
  attribute \src "./reqwalker.py:278"
  cell $mux $424
    parameter \WIDTH 3'101
    connect \A $417
    connect \B 5'00000
    connect \S $422
    connect \Y $419
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $425
  attribute \src "./reqwalker.py:278"
  cell $eq $426
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B $419
    connect \Y $425
  end
  attribute \src "./reqwalker.py:278"
  cell $assert $427
    connect \A $assert$check$406
    connect \EN $assert$en$405
  end
  process $group_64
    assign $assert$en$405 1'0
    assign $assert$check$406 1'0
    attribute \src "./reqwalker.py:276"
    switch { $413 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$406 $425
        assign $assert$en$405 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$en$428
  attribute \src "./reqwalker.py:277"
  wire width 1 $assert$check$429
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:275"
  wire width 4 $sample$s$state$sync$4
  attribute \src "./reqwalker.py:275"
  wire width 4 $sample$s$state$sync$4$next
  attribute \src "./reqwalker.py:275"
  wire width 1 $430
  attribute \src "./reqwalker.py:275"
  cell $ne $431
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$4
    connect \B 1'0
    connect \Y $430
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $432
  attribute \src "./reqwalker.py:275"
  cell $and $433
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $430
    connect \Y $432
  end
  attribute \nmigen.sample_reg 1
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$4
  attribute \src "./reqwalker.py:276"
  wire width 32 $sample$s$counter$sync$4$next
  attribute \src "./reqwalker.py:276"
  wire width 1 $434
  attribute \src "./reqwalker.py:276"
  cell $eq $435
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$4
    connect \B 1'0
    connect \Y $434
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $436
  attribute \src "./reqwalker.py:276"
  cell $and $437
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $432
    connect \B $434
    connect \Y $436
  end
  attribute \src "./reqwalker.py:277"
  wire width 1 $438
  attribute \src "./reqwalker.py:277"
  cell $eq $439
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'100
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$1
    connect \B $sample$s$state$sync$4
    connect \Y $438
  end
  attribute \src "./reqwalker.py:277"
  cell $assert $440
    connect \A $assert$check$429
    connect \EN $assert$en$428
  end
  process $group_66
    assign $assert$en$428 1'0
    assign $assert$check$429 1'0
    attribute \src "./reqwalker.py:276"
    switch { $436 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$429 $438
        assign $assert$en$428 1'1
    end
    sync init
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$en$441
  attribute \src "./reqwalker.py:278"
  wire width 1 $assert$check$442
  attribute \src "./reqwalker.py:275"
  wire width 1 $443
  attribute \src "./reqwalker.py:275"
  cell $ne $444
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$state$sync$4
    connect \B 1'0
    connect \Y $443
  end
  attribute \src "./reqwalker.py:275"
  wire width 1 $445
  attribute \src "./reqwalker.py:275"
  cell $and $446
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A \f_pastn_valid
    connect \B $443
    connect \Y $445
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $447
  attribute \src "./reqwalker.py:276"
  cell $eq $448
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 6'100000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $sample$s$counter$sync$4
    connect \B 1'0
    connect \Y $447
  end
  attribute \src "./reqwalker.py:276"
  wire width 1 $449
  attribute \src "./reqwalker.py:276"
  cell $and $450
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 1'1
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $445
    connect \B $447
    connect \Y $449
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $451
  attribute \src "./reqwalker.py:278"
  cell $add $452
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$4
    connect \B 1'1
    connect \Y $451
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $453
  attribute \src "./reqwalker.py:278"
  cell $mod $454
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 3'101
    connect \A $451
    connect \B 5'10000
    connect \Y $453
  end
  attribute \src "./reqwalker.py:278"
  wire width 5 $455
  attribute \src "./reqwalker.py:278"
  wire width 5 $456
  attribute \src "./reqwalker.py:278"
  cell $add $457
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 3'101
    connect \A $sample$s$state$sync$4
    connect \B 1'1
    connect \Y $456
  end
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  wire width 1 $458
  attribute \src "/nix/store/p8bl7qnjw0czgpmmwinsbknm2c7yq6sc-python3.7-nmigen-unstable-2019-02-08/lib/python3.7/site-packages/nmigen/back/rtlil.py:525"
  cell $eq $459
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'101
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 1'1
    connect \A $456
    connect \B 1'0
    connect \Y $458
  end
  attribute \src "./reqwalker.py:278"
  cell $mux $460
    parameter \WIDTH 3'101
    connect \A $453
    connect \B 5'00000
    connect \S $458
    connect \Y $455
  end
  attribute \src "./reqwalker.py:278"
  wire width 1 $461
  attribute \src "./reqwalker.py:278"
  cell $eq $462
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 3'100
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 3'101
    parameter \Y_WIDTH 1'1
    connect \A \state
    connect \B $455
    connect \Y $461
  end
  attribute \src "./reqwalker.py:278"
  cell $assert $463
    connect \A $assert$check$442
    connect \EN $assert$en$441
  end
  process $group_68
    assign $assert$en$441 1'0
    assign $assert$check$442 1'0
    attribute \src "./reqwalker.py:276"
    switch { $449 }
      attribute \src "./reqwalker.py:276"
      case 1'1
        assign $assert$check$442 $461
        assign $assert$en$441 1'1
    end
    sync init
  end
  process $group_70
    assign $sample$s$state$sync$1$next $sample$s$state$sync$1
    assign $sample$s$state$sync$1$next \state
    sync init
      update $sample$s$state$sync$1 4'0000
    sync posedge \clk
      update $sample$s$state$sync$1 $sample$s$state$sync$1$next
  end
  process $group_71
    assign $sample$s$counter$sync$1$next $sample$s$counter$sync$1
    assign $sample$s$counter$sync$1$next \counter
    sync init
      update $sample$s$counter$sync$1 32'00000000000000000000000000000000
    sync posedge \clk
      update $sample$s$counter$sync$1 $sample$s$counter$sync$1$next
  end
  process $group_72
    assign $sample$s$i_req$sync$1$next $sample$s$i_req$sync$1
    assign $sample$s$i_req$sync$1$next \i_req
    sync init
      update $sample$s$i_req$sync$1 1'0
    sync posedge \clk
      update $sample$s$i_req$sync$1 $sample$s$i_req$sync$1$next
  end
  process $group_73
    assign $sample$s$state$sync$2$next $sample$s$state$sync$2
    assign $sample$s$state$sync$2$next $sample$s$state$sync$1
    sync init
      update $sample$s$state$sync$2 4'0000
    sync posedge \clk
      update $sample$s$state$sync$2 $sample$s$state$sync$2$next
  end
  process $group_74
    assign $sample$s$counter$sync$2$next $sample$s$counter$sync$2
    assign $sample$s$counter$sync$2$next $sample$s$counter$sync$1
    sync init
      update $sample$s$counter$sync$2 32'00000000000000000000000000000000
    sync posedge \clk
      update $sample$s$counter$sync$2 $sample$s$counter$sync$2$next
  end
  process $group_75
    assign $sample$s$state$sync$3$next $sample$s$state$sync$3
    assign $sample$s$state$sync$3$next $sample$s$state$sync$2
    sync init
      update $sample$s$state$sync$3 4'0000
    sync posedge \clk
      update $sample$s$state$sync$3 $sample$s$state$sync$3$next
  end
  process $group_76
    assign $sample$s$counter$sync$3$next $sample$s$counter$sync$3
    assign $sample$s$counter$sync$3$next $sample$s$counter$sync$2
    sync init
      update $sample$s$counter$sync$3 32'00000000000000000000000000000000
    sync posedge \clk
      update $sample$s$counter$sync$3 $sample$s$counter$sync$3$next
  end
  process $group_77
    assign $sample$s$state$sync$4$next $sample$s$state$sync$4
    assign $sample$s$state$sync$4$next $sample$s$state$sync$3
    sync init
      update $sample$s$state$sync$4 4'0000
    sync posedge \clk
      update $sample$s$state$sync$4 $sample$s$state$sync$4$next
  end
  process $group_78
    assign $sample$s$counter$sync$4$next $sample$s$counter$sync$4
    assign $sample$s$counter$sync$4$next $sample$s$counter$sync$3
    sync init
      update $sample$s$counter$sync$4 32'00000000000000000000000000000000
    sync posedge \clk
      update $sample$s$counter$sync$4 $sample$s$counter$sync$4$next
  end
end

