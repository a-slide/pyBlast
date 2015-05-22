# -*- coding: utf-8 -*-

"""
@package    pyBlast
@brief      Class to represent the informations from a blast hit
@copyright  [GNU General Public License v2](http://www.gnu.org/licenses/gpl-2.0.html)
@author     Adrien Leger - 2014
* <adrien.leger@gmail.com> <adrien.leger@inserm.fr> <adrien.leger@univ-nantes.fr>
* [Github](https://github.com/a-slide)
* [Atlantic Gene Therapies - INSERM 1089] (http://www.atlantic-gene-therapies.fr/)
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class BlastHit(object):
    """
    @class  BlastHit
    @brief  Object oriented class containing informations of one blast hit
    """
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~~~~~~CLASS FIELDS~~~~~~~#
    ID_COUNT = 0

    #~~~~~~~CLASS METHODS~~~~~~~#

    @ classmethod
    def next_id (self):
        cur_id = self.ID_COUNT
        self.ID_COUNT +=1
        return cur_id

    #~~~~~~~FONDAMENTAL METHODS~~~~~~~#

    def __init__(self,
        q_id = "query",
        s_id = "subject",
        identity = 100,
        length = 0,
        mis = 0,
        gap = 0,
        q_start = 0,
        q_end = 0,
        s_start = 0,
        s_end = 0,
        evalue = 0,
        bscore = 0,
        q_seq = "ATCG"):
        """
        Create a BlastHit object which is automatically added to the class tracking instance list
        The object with the following parameters are required for object initialisation
        @param  q_id    Query sequence name
        @param  s_id    Subject sequence name
        @param  identity    % of identity in the hit
        @param  length  length of the hit
        @param  mis Number of mismatch in the hit
        @param  gap Number of gap in the hit
        @param  q_start Hit start position of the query
        @param  q_end   Hit end position of the query
        @param  s_start Hit start position of the subject
        @param  s_end   Hit end position of the subject
        @param  evalue  E value of the alignement
        @param  bscore Bit score of the alignement
        @param  q_seq Sequence of the query aligned on the subject sequence
        """

        # Store parameters in self variables
        self.id = self.next_id()
        self.q_id = q_id
        self.s_id = s_id
        self.identity = float(identity)
        self.length = int(length)
        self.mis = int(mis)
        self.gap = int(gap)
        self.evalue = float(evalue)
        self.bscore = float(bscore)
        self.q_seq = q_seq

        # Correct coordinates of hit for python 0 based coordinates depending of the orientation
        if int(q_start) < int(q_end):
            self.q_orient = "+"
            self.q_start = int(q_start)-1
            self.q_end = int(q_end)
        else:
            self.q_orient = "-"
            self.q_start = int(q_start)
            self.q_end = int(q_end)-1

        if int(s_start) < int(s_end):
            self.s_orient = "+"
            self.s_start = int(s_start)-1
            self.s_end = int(s_end)
        else:
            self.s_orient = "-"
            self.s_start = int(s_start)
            self.s_end = int(s_end)-1

        # Verify the hit validity
        self._test_arg()

    def __str__(self):
        msg = "HIT {}".format(self.id)
        msg += "\tQuery\t{}:{}-{}({})\n".format(self.q_id, self.q_start, self.q_end, self.q_orient)
        msg += "\tSubject\t{}:{}-{}({})\n".format(self.s_id, self.s_start, self.s_end, self.s_orient)
        msg += "\tLenght : {}\tIdentity : {}%\tEvalue : {}\tBit score : {}\n".format(self.length, self.identity, self.evalue, self.bscore)
        msg += "\tAligned query seq : {}\n".format(self.q_seq)
        return (msg)

    def __repr__(self):
        return "<Instance of {} from {} >\n".format(self.__class__.__name__, self.__module__)

    #~~~~~~~PRIVATE METHODS~~~~~~~#

    def _test_arg(self):
        assert 0 <= self.identity <= 100, "Identity value out of range [0:100]"
        assert self.length > -1, "length value out of range [>= 0]"
        assert self.mis > -1, "mis value out of range [>= 0]"
        assert self.gap > -1, "gap value out of range [>= 0]"
        assert self.q_start > -1, "q_start value out of range [>= 0]"
        assert self.q_end > -1, "q_end value out of range [>= 0]"
        assert self.s_start > -1, "s_start value out of range [>= 0]"
        assert self.s_end > -1, "s_end value out of range [>= 0]"
        assert self.evalue > -1, "evalue value out of range [>= 0]"
        assert self.bscore > -1, "bscore value out of range [>= 0]"