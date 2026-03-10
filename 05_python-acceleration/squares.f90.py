module squares_mod
  implicit none
contains

  function sum_of_squares(n) result(res)
    integer, intent(in) :: n
    integer :: res
    integer :: i

    res = 0
    do i = 1, n
       res = res + i*i
    end do

  end function sum_of_squares

end module squares_mod